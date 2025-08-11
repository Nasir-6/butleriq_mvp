# ButlerIQ - Hotel Voice Request System

A voice-enabled request system for hotel guests, built with FastAPI, Supabase, and React.

## Dependencies

### Backend Dependencies
- **Python 3.9+** - Core programming language
- **FastAPI 0.95.2** - Modern web framework for building APIs
- **Uvicorn 0.22.0** - ASGI server for running FastAPI applications
- **Pydantic 1.10.7** - Data validation and settings management
- **python-dotenv 1.0.0** - Loads environment variables from .env files

For complete list with versions, see [requirements.txt](./backend/requirements.txt)

### Frontend Dependencies (Coming Soon)
- React
- Node.js 16+

## Project Structure

```
butleriq_mvp/
├── backend/                 # FastAPI backend
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py         # FastAPI application
│   │   ├── config.py       # Configuration settings
│   │   ├── database.py     # Database connection
│   │   └── models/         # Database models
│   ├── requirements.txt    # Python dependencies
│   └── .env.example       # Example environment variables
│
├── frontend/               # React frontend (to be added)
│   ├── staff-dashboard/    # Staff interface
│   └── guest-dashboard/    # Guest interface
│
└── docs/                   # Documentation
    └── api.md             # API documentation
```

## Getting Started

### Prerequisites
- Python 3.9+
- Node.js 16+ (for frontend)
- Supabase account
- Home Assistant (for voice integration)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/butleriq_mvp.git
   cd butleriq_mvp
   ```

2. **Set up the backend**
   ```bash
   # Navigate to backend directory
   cd backend
   
   # Create and activate virtual environment
   python -m venv venv
   source venv/bin/activate  # On Windows: .\venv\Scripts\activate
   
   # Install Python dependencies
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   ```bash
   # Copy the example environment file
   cp .env.example .env
   
   # Edit the .env file with your Supabase credentials
   ```

4. **Run the development server**
   ```bash
   uvicorn app.main:app --reload
   ```
   The API will be available at http://localhost:8000

5. **API Documentation**
   - Interactive API docs: http://localhost:8000/docs
   - Alternative API docs: http://localhost:8000/redoc

## Development

### Backend
```bash
cd backend
uvicorn app.main:app --reload
```

### Frontend
```bash
cd frontend/staff-dashboard
npm install
npm start
```

## API Documentation

Once the server is running, visit:
- API docs: http://localhost:8000/docs
- Redoc: http://localhost:8000/redoc
