from pydantic_settings import BaseSettings
from functools import lru_cache
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Settings(BaseSettings):
    # API settings
    APP_NAME: str = "ButlerIQ Voice API"
    DEBUG: bool = os.getenv("DEBUG", "False").lower() in ("true", "1", "t")
    
    # CORS settings
    ALLOWED_ORIGINS: list = ["*"]  # For development only
    
    # Home Assistant settings
    HA_WEBHOOK_URL: str = os.getenv("HA_WEBHOOK_URL")
    
    # Supabase settings
    SUPABASE_URL: str = os.getenv("SUPABASE_URL")
    SUPABASE_KEY: str = os.getenv("SUPABASE_KEY")
    
    class Config:
        env_file = ".env"
        case_sensitive = True

@lru_cache()
def get_settings() -> Settings:
    """
    Get application settings, cached for performance.
    """
    return Settings()
