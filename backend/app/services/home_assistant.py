import logging
import os
import requests
from typing import Dict, Any

logger = logging.getLogger(__name__)

class HomeAssistantService:

    def __init__(self):
        self.base_url = os.getenv("HA_WEBHOOK_URL")
        if not self.base_url:
            raise RuntimeError("HomeAssistantService cannot be initialized: HA_WEBHOOK_URL environment variable is not set")
    
    def respond_via_webhook(self, data: Dict[str, Any]) -> bool:
        try:
            response = requests.post(
                self.base_url,
                json=data,
                verify=False  # Only for development with self-signed certs
            )
            
            logger.info(f"Sent webhook to Home Assistant. Status: {response.status_code}")
            logger.info(f"Response: {response.text}")
            
            return response.ok
            
        except requests.exceptions.RequestException as e:
            logger.error(f"Error sending webhook to Home Assistant: {str(e)}")
            raise

# Create a default instance for easier importing
try:
    ha_service = HomeAssistantService()
except RuntimeError as e:
    import sys
    print(f"Error: {str(e)}", file=sys.stderr)
    sys.exit(1)
