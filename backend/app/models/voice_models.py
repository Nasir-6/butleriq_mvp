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
        status: Status of the operation (e.g., 'success', 'error')
        message: Response message to be sent back to the client
        intent: Detected intent of the voice command
    """
    status: str
    message: str
    intent: str
