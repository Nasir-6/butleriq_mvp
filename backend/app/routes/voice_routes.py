from fastapi import APIRouter, HTTPException, Depends
from app.models.voice_models import VoiceCommand, VoiceResponse
from app.services.home_assistant import ha_service as home_assistant_service
import logging

logger = logging.getLogger(__name__)
router = APIRouter(
    prefix="/api/v1",
    tags=["voice"],
    responses={404: {"description": "Not found"}},
)

@router.get("/")
async def root():
    """Root endpoint with API information."""
    return {
        "message": "ButlerIQ Voice API is running",
        "endpoints": {
            "POST /voice-command": "Process voice commands",
            "GET /health": "Check API status"
        }
    }

@router.post("/voice-command", response_model=VoiceResponse)
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
        
        # Send response back to Home Assistant via webhook
        home_assistant_service.respond_via_webhook(response)
        return response
        
    except Exception as e:
        logger.error(f"Error processing command: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))
