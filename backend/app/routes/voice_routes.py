from fastapi import APIRouter, HTTPException
from app.models.voice_models import VoiceCommand, VoiceResponse
from app.services.home_assistant import ha_service as home_assistant_service
from app.nlp.nlp_service import nlp_service
import logging

logger = logging.getLogger(__name__)
router = APIRouter(
    prefix="/api/v1",
    tags=["voice"],
    responses={404: {"description": "Not found"}},
)

# Map predicted label to response text and intent
DEPARTMENT_RESPONSES = {
    "Housekeeping": {
        "message": "Housekeeping has been notified and will assist you shortly.",
        "intent": "housekeeping_request"
    },
    "Maintenance": {
        "message": "Maintenance has been notified about the issue.",
        "intent": "maintenance_request"
    },
    "Room Service": {
        "message": "Room Service has received your order request.",
        "intent": "room_service_request"
    },
    "Front Desk": {
        "message": "The front desk has been notified about your request.",
        "intent": "front_desk_request"
    },
    "Concierge": {
        "message": "Concierge has received your request.",
        "intent": "concierge_request"
    },
    "General Help": {
        "message": "Your request has been received and will be handled by our staff shortly.",
        "intent": "general_request"
    }
}

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
    Handle voice commands from Home Assistant using ML model.
    """
    try:
        # Predict the department using the NLPService with fallback to 'General Help'
        predicted_department = nlp_service.predict_department(command.text) or "General Help"
        
        # Get response details, defaulting to General Help if department not found
        response_details = DEPARTMENT_RESPONSES.get(predicted_department)
        
        # Send webhook to Home Assistant
        webhook_data = {
            "intent": response_details["intent"],
            "text": command.text,
            "department": predicted_department,
            "room_number": command.room_number,
            "message": response_details["message"]
        }
        home_assistant_service.respond_via_webhook(webhook_data)
        
        return VoiceResponse(
            text=response_details["message"],
            department=predicted_department,
            confidence=1.0  # NLPService can be updated to return confidence if needed
        )
        
    except Exception as e:
        logger.error(f"Error processing voice command: {str(e)}", exc_info=True)
        raise HTTPException(
            status_code=500,
            detail=f"Error processing voice command: {str(e)}"
        )
