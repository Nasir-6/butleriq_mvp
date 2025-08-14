from pydantic import BaseModel
from typing import Optional

class VoiceCommand(BaseModel):
    """
    Model representing a voice command received from the client.
    
    Attributes:
        text: The transcribed text of the voice command
        room_number: The room number where the command originated
        device_id: Optional device identifier
    """
    text: str
    room_number: str
    device_id: Optional[str] = None

class VoiceResponse(BaseModel):
    """
    Model representing the response to a voice command.
    
    Attributes:
        text: The response message to be spoken
        department: The predicted department
        confidence: Confidence score of the prediction (0.0 to 1.0)
    """
    text: str
    department: str
    confidence: float
