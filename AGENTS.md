# Custody Management System

## Project Overview
This is a criminal records and evidence management system. It has been upgraded from a client-side only application (using localStorage) to a full-stack application with a FastAPI backend and SQLite database.

## Architecture
- **Backend**: FastAPI (Python) with `uv` package manager.
- **Database**: SQLite (file-based).
- **Frontend**: Vanilla HTML/CSS/JS served by FastAPI's StaticFiles.
- **Authentication**: JWT (JSON Web Tokens) with `python-jose` and `bcrypt` for password hashing.
- **File Storage**: Files are stored locally in the `backend/uploads/` directory.

## Project Structure
```
/home/vagabond/CustodyManagement
├── backend/
│   ├── app/
│   │   ├── main.py           # FastAPI app entrypoint
│   │   ├── config.py         # Configuration (DB URL, Secret Key)
│   │   ├── database.py       # SQLAlchemy engine and session
│   │   ├── models.py         # SQLAlchemy models (User, Document)
│   │   ├── schemas.py        # Pydantic models (Request/Response)
│   │   ├── crud.py           # Database operations
│   │   ├── routes/
│   │   │   ├── auth.py       # Authentication endpoints
│   │   │   └── documents.py  # Document/Evidence handling
│   │   └── middleware.py     # CORS, Logging
│   ├── uploads/              # Directory for storing uploaded files
│   ├── data/                 # Directory for SQLite database file
│   ├── .env                  # Environment variables
│   └── pyproject.toml        # Project dependencies (uv format)
├── frontend/
│   ├── index.html            # Login/Signup page
│   ├── dashboard.html        # User dashboard
│   ├── admin.html            # Admin panel
│   ├── blog.html             # Blog page
│   ├── about.html            # About page
│   ├── style.css             # Global styles
│   ├── script.js             # Auth logic
│   ├── dashboard.js          # Dashboard logic
│   └── admin.js              # Admin logic
└── AGENTS.md                 # This file
```

## Setup and Running
1.  **Install Dependencies**:
    ```bash
    cd backend
    uv sync
    ```
2.  **Run Backend**:
    ```bash
    cd backend
    uv run uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
    ```
3.  **Access Frontend**:
    Open `http://localhost:8000/static/index.html` in your browser.

## Key Features
- **User Authentication**: Register and login with JWT.
- **Document Management**: Upload, view, and delete evidence files.
- **Admin Panel**: View all documents, mark cases as solved, delete files.
- **Dark Mode**: Toggle between light and dark themes.

## Notes
- The database is SQLite and located at `backend/data/db.sqlite3`.
- Uploaded files are stored in `backend/uploads/`.
- CORS is configured to allow requests from `localhost:5500` and `null` (file protocol).
