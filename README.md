# Custody Management System

A secure, full-stack criminal records and evidence management system built with FastAPI (Python) and Vanilla JavaScript.

## Features

- **Secure Authentication**: JWT-based authentication with bcrypt password hashing.
- **Evidence Management**: Upload, view, and delete digital evidence files.
- **Case Tracking**: Mark cases as solved and track case numbers.
- **Admin Panel**: Manage all documents and user permissions.
- **Dark Mode**: Toggle between light and dark themes.
- **Responsive Design**: Works on desktop and mobile devices.

## Architecture

- **Backend**: FastAPI (Python) with SQLite database
- **Frontend**: Vanilla HTML/CSS/JS
- **Authentication**: JWT (JSON Web Tokens)
- **File Storage**: Local filesystem (`backend/uploads/`)

## Project Structure

```
CustodyManagement/
├── backend/                  # FastAPI backend application
│   ├── app/
│   │   ├── main.py          # FastAPI entrypoint
│   │   ├── config.py        # Configuration settings
│   │   ├── database.py      # SQLAlchemy database setup
│   │   ├── models.py        # Database models
│   │   ├── schemas.py       # Pydantic schemas
│   │   ├── crud.py          # Database operations
│   │   └── routes/          # API routes
│   │       ├── auth.py      # Authentication endpoints
│   │       └── documents.py # Document management endpoints
│   ├── uploads/             # Uploaded files storage
│   ├── data/                # SQLite database file
│   └── pyproject.toml       # Python dependencies
├── frontend/                # Frontend static files
│   ├── index.html          # Login/Signup page
│   ├── dashboard.html      # User dashboard
│   ├── admin.html          # Admin panel
│   ├── blog.html           # Blog page
│   ├── about.html          # About page
│   ├── style.css           # Global styles
│   ├── script.js           # Authentication logic
│   ├── dashboard.js        # Dashboard functionality
│   └── admin.js            # Admin panel functionality
├── run.py                  # Python startup script (Linux/Mac)
├── run.bat                 # Batch startup script (Windows)
├── AGENTS.md               # Project documentation
└── README.md               # This file
```

## Installation & Setup

### Prerequisites

- Python 3.14+
- `uv` package manager (recommended)

### Backend Setup

1. Navigate to the backend directory:
   ```bash
   cd backend
   ```

2. Install dependencies using `uv`:
   ```bash
   uv sync
   ```

3. Create the necessary directories (if they don't exist):
   ```bash
   mkdir -p uploads data
   ```

### Frontend Setup

The frontend is served directly by FastAPI from the `frontend/` directory. No additional setup is required.

## Running the Application

### Quick Start (Recommended)

Run the startup script from the project root directory:

**Linux/Mac:**
```bash
python run.py
```

**Windows:**
```cmd
run.bat
```

This script will:
1. Check for required dependencies (uv)
2. Setup the backend virtual environment
3. Create necessary directories (uploads, data)
4. Start the FastAPI server with auto-reload

### Script Options

The Python run script supports several options:

```bash
# Use custom port
python run.py --port 8080

# Bind to specific host
python run.py --host 127.0.0.1

# Disable auto-reload (for production)
python run.py --no-reload

# Show help
python run.py --help
```

### Manual Start

Alternatively, you can start the backend server manually:

From the `backend` directory:
```bash
uv run uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### Access the Application

Once the server is running, open your browser and navigate to:
```
http://localhost:8000/static/index.html
```

The application will be available at:
- **Frontend**: http://localhost:8000/static/index.html
- **API Docs**: http://localhost:8000/docs
- **Backend**: http://localhost:8000

## API Endpoints

### Authentication

- `POST /auth/register` - Register a new user
- `POST /auth/login` - Login and receive JWT token
- `GET /auth/users/me` - Get current user information

### Documents

- `POST /documents/upload` - Upload a new document/evidence file
- `GET /documents/` - List all documents
- `GET /documents/{id}` - Get document metadata
- `GET /documents/{id}/file` - Download document file
- `PATCH /documents/{id}/status` - Update document status (e.g., mark as solved)
- `DELETE /documents/{id}` - Delete a document

## Usage

### User Registration

1. Navigate to the homepage
2. Fill in the registration form with username, email, and password
3. Click "Sign Up"
4. You will be redirected to the login page

### User Login

1. Enter your username and password
2. Click "Login"
3. You will be redirected to the dashboard

### Uploading Evidence

1. On the dashboard, fill in the evidence title
2. Optional: Add a case number
3. Select a file to upload
4. Click "Upload"
5. The file will appear in the documents grid

### Managing Documents

- **Preview**: Click "Preview" to view file details
- **Delete**: Click "Delete" to remove a document
- **Search**: Use the search bar to find documents
- **Sort**: Use the dropdown to sort documents by date, name, or size

### Admin Features

1. Navigate to the Admin panel (`/static/admin.html`)
2. Login with admin credentials
3. View all documents from all users
4. Mark cases as solved
5. Delete documents

## Security Features

- **JWT Authentication**: Secure token-based authentication
- **Password Hashing**: bcrypt hashing for user passwords
- **CORS Configuration**: Restricted to trusted origins
- **File Type Validation**: Server-side file type checking
- **Authorization**: Users can only modify their own documents (admins have full access)

## Database Schema

### Users Table
- `id` - Primary key
- `username` - Unique username
- `email` - Unique email address
- `hashed_password` - bcrypt hashed password
- `role` - User role (admin/officer)
- `created_at` - Account creation timestamp

### Documents Table
- `id` - Primary key
- `title` - Document title
- `filename` - Stored filename
- `file_path` - Filesystem path
- `file_type` - MIME type
- `file_size` - File size in bytes
- `case_number` - Associated case number
- `status` - Case status (open/solved)
- `uploaded_by_id` - Foreign key to users
- `uploaded_at` - Upload timestamp
- `case_solved_number` - Solved case reference

## Environment Variables

Create a `.env` file in the `backend/` directory:

```env
DATABASE_URL=sqlite:///./data/db.sqlite3
SECRET_KEY=your-secret-key-change-in-production
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

## Development

### Code Structure

- **Backend**: Follows FastAPI best practices with routers, models, and schemas separated
- **Frontend**: Modular JavaScript with clear separation of concerns

### Adding New Features

1. **Backend**: Add new routes in `app/routes/`
2. **Frontend**: Add new pages in `frontend/` and update JavaScript files
3. **Database**: Update models in `app/models.py` and create migrations

## Troubleshooting

### Database Issues

If you encounter database errors:
1. Stop the server
2. Delete the `backend/data/db.sqlite3` file
3. Restart the server (database will be recreated)

### File Upload Issues

Ensure the `backend/uploads/` directory exists and has write permissions.

### Authentication Issues

Clear browser localStorage if you encounter login problems:
```javascript
localStorage.clear();
```

## License

This project is for educational purposes.

## Contact

For questions or issues, please refer to the project documentation.
