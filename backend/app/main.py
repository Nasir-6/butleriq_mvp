from fastapi import FastAPI, HTTPException, Request  # Added Request here
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
import logging
import uvicorn
import requests
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get HA_WEBHOOK_URL from environment variables
HA_WEBHOOK_URL = os.getenv("HA_WEBHOOK_URL")
if not HA_WEBHOOK_URL:
    raise ValueError("HA_WEBHOOK_URL environment variable is not set")

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize FastAPI app
app = FastAPI(
    title="ButlerIQ Voice API",
    description="Minimal API for Home Assistant voice commands",
    version="0.1.0"
)

# CORS middleware - allow all origins for development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Models
class VoiceCommand(BaseModel):
    text: str
    room_number: str
    device_id: Optional[str] = None

class VoiceResponse(BaseModel):
    status: str
    message: str
    intent: str


def send_reply_to_ha(json):
    try:
        r = requests.post(HA_WEBHOOK_URL, json=json, verify=False)
        print(f"Status code: {r.status_code}")
        print(f"Response body: {r.text}")
    except Exception as e:
        print("Error:", e)



# Routes
@app.get("/")
async def root():
    return {
        "message": "ButlerIQ Voice API is running",
        "endpoints": {
            "POST /voice-command": "Process voice commands",
            "GET /health": "Check API status"
        }
    }


@app.post("/voice-command", response_model=VoiceResponse)
async def handle_voice_command(command: VoiceCommand):
    """
    Handle voice commands from Home Assistant.
    """
    try:
        logger.info(f"Received command from room {command.room_number}: {command.text}")
        
        # Simple intent detection
        text = command.text.lower()
        
        if any(word in text for word in ["clean", "towel", "housekeeping"]):
            response = {
                "status": "success",
                "message": "Housekeeping has been notified and will assist you shortly.",
                "intent": "housekeeping_request"
            }
        elif any(word in text for word in ["light", "electric", "maintenance"]):
            response = {
                "status": "success",
                "message": "Maintenance has been notified about the issue.",
                "intent": "maintenance_request"
            }
        else:
            response = {
                "status": "success",
                "message": "Your request has been received by our staff.",
                "intent": "general_request"
            }
        
        logger.info(f"Response: {response}")
        send_reply_to_ha(response)
        
        return response
        
    except Exception as e:
        logger.error(f"Error processing command: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

     
@app.get("/health")
async def health_check():
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
