from fastapi import FastAPI, HTTPException, Request  # Added Request here
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
import logging
import json  # Added json import
import uvicorn

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
        return response
        
    except Exception as e:
        logger.error(f"Error processing command: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

# @app.post("/voice-command")
# async def handle_voice_command(request: Request):
#     """
#     Debug endpoint to log raw request data
#     """
#     try:
#         # Log request details
#         print("\n=== REQUEST DETAILS ===")
#         print(f"Method: {request.method}")
#         print(f"Headers: {dict(request.headers)}")
#         print(f"Client: {request.client}")
        
#         # Try to get JSON body
#         try:
#             body = await request.json()
#             print("\n=== JSON BODY ===")
#             print(body)
#         except Exception as e:
#             print(f"\nCould not parse JSON: {e}")
#             body = await request.body()
#             print("\n=== RAW BODY ===")
#             print(body.decode())
        
#         # Try to get form data
#         try:
#             form_data = await request.form()
#             print("\n=== FORM DATA ===")
#             print(dict(form_data))
#         except Exception:
#             pass
            
#         return {
#             "status": "debug",
#             "message": "Check server logs for request details"
#         }
        
#     except Exception as e:
#         print(f"\n=== ERROR ===")
#         print(str(e))
#         return {"error": str(e)}   

     
@app.get("/health")
async def health_check():
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
