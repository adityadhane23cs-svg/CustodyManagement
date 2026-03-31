@echo off
REM Custody Management System - Startup Script for Windows

echo.
echo ╔════════════════════════════════════════════════════════════════╗
echo ║                                                                ║
echo ║        CUSTODY MANAGEMENT SYSTEM - STARTUP SCRIPT             ║
echo ║                                                                ║
echo ║  Criminal Records & Evidence Management System                 ║
echo ║  FastAPI Backend + Static Frontend                             ║
echo ║                                                                ║
echo ╚════════════════════════════════════════════════════════════════╝
echo.

REM Check if backend directory exists
if not exist "backend" (
    echo ✗ Backend directory not found
    pause
    exit /b 1
)

REM Check if uv is installed
uv --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ✗ uv package manager not found
    echo   Please install uv: curl -LsSf https://astral.sh/uv/install.sh ^| sh
    pause
    exit /b 1
)

echo Setting up backend...
cd backend

REM Create directories if they don't exist
if not exist "uploads" mkdir uploads
if not exist "data" mkdir data

REM Check if virtual environment exists
if not exist ".venv" (
    echo   Creating virtual environment...
    uv sync
) else (
    echo   Virtual environment already exists
)

echo ✓ Backend setup complete
echo.

echo Starting FastAPI backend server...
echo   Server URL: http://localhost:8000
echo   Frontend:   http://localhost:8000/static/index.html
echo   API Docs:   http://localhost:8000/docs
echo.
echo Press Ctrl+C to stop the server
echo.

uv run uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload

pause
