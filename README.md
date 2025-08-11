# ButlerIQ - Hotel Voice Request System

A voice-enabled request system for hotel guests, built with FastAPI, Supabase, and React.

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

1. Clone the repository
2. Set up the backend:
   ```bash
   cd backend
   python -m venv venv
   source venv/bin/activate  # On Windows: .\venv\Scripts\activate
   pip install -r requirements.txt
   ```
3. Set up environment variables:
   ```bash
   cp .env.example .env
   # Edit .env with your Supabase credentials
   ```

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
