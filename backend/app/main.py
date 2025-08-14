from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import logging
import uvicorn
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Import routers
from app.routes.voice_routes import router as voice_router

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

# Include routers
app.include_router(voice_router)

@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {
        "status": "healthy",
        "version": "0.1.0"
    }

@app.get("/")
async def root():
    """Root endpoint with API information."""
    return {
        "message": "ButlerIQ Voice API is running",
        "documentation": "/docs",
        "endpoints": {
            "POST /api/v1/voice-command": "Process voice commands",
            "GET /health": "Check API status"
        }
    }

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
