#!/usr/bin/env python3
"""
Custody Management System - Startup Script

This script starts the FastAPI backend server which also serves the frontend static files.
"""

import subprocess
import sys
import os
import time
import argparse
from pathlib import Path


def print_banner():
    """Print the application banner."""
    banner = """
    ╔════════════════════════════════════════════════════════════════╗
    ║                                                                ║
    ║        CUSTODY MANAGEMENT SYSTEM - STARTUP SCRIPT             ║
    ║                                                                ║
    ║  Criminal Records & Evidence Management System                 ║
    ║  FastAPI Backend + Static Frontend                             ║
    ║                                                                ║
    ╚════════════════════════════════════════════════════════════════╝
    """
    print(banner)


def check_dependencies():
    """Check if required dependencies are installed."""
    print("Checking dependencies...")

    # Check if uv is installed
    try:
        subprocess.run(["uv", "--version"], check=True, capture_output=True)
        print("✓ uv package manager found")
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("✗ uv package manager not found")
        print("  Please install uv: curl -LsSf https://astral.sh/uv/install.sh | sh")
        return False

    return True


def setup_backend():
    """Setup the backend dependencies if needed."""
    backend_dir = Path("backend")

    if not backend_dir.exists():
        print("✗ Backend directory not found")
        return False

    print("Setting up backend...")

    # Check if virtual environment exists
    venv_dir = backend_dir / ".venv"
    if not venv_dir.exists():
        print("  Creating virtual environment...")
        subprocess.run(["uv", "sync"], cwd=backend_dir, check=True)
    else:
        print("  Virtual environment already exists")

    # Check if uploads directory exists
    uploads_dir = backend_dir / "uploads"
    if not uploads_dir.exists():
        print("  Creating uploads directory...")
        uploads_dir.mkdir(parents=True, exist_ok=True)

    # Check if data directory exists
    data_dir = backend_dir / "data"
    if not data_dir.exists():
        print("  Creating data directory...")
        data_dir.mkdir(parents=True, exist_ok=True)

    print("✓ Backend setup complete")
    return True


def start_backend(args):
    """Start the FastAPI backend server."""
    backend_dir = Path("backend")

    server_url = f"http://{args.host}:{args.port}"
    frontend_url = f"{server_url}/static/index.html"
    docs_url = f"{server_url}/docs"

    print("\nStarting FastAPI backend server...")
    print(f"  Server URL: {server_url}")
    print(f"  Frontend:   {frontend_url}")
    print(f"  API Docs:   {docs_url}")
    print("\nPress Ctrl+C to stop the server\n")
    print("-" * 60)

    try:
        # Build command
        cmd = [
            "uv",
            "run",
            "uvicorn",
            "app.main:app",
            "--host",
            args.host,
            "--port",
            str(args.port),
        ]

        if not args.no_reload:
            cmd.append("--reload")

        # Start the server
        subprocess.run(cmd, cwd=backend_dir, check=True)
    except subprocess.CalledProcessError as e:
        print(f"\n✗ Server stopped with error: {e}")
        return False
    except KeyboardInterrupt:
        print("\n\nShutting down server...")
        return True

    return True

    return True


def parse_arguments():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description="Start the Custody Management System backend server",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python run.py                 # Start with default settings
  python run.py --port 8080     # Use custom port
  python run.py --no-reload     # Disable auto-reload
  python run.py --host 127.0.0.1 # Bind to specific host
        """,
    )

    parser.add_argument(
        "--port",
        "-p",
        type=int,
        default=8000,
        help="Port to run the server on (default: 8000)",
    )

    parser.add_argument(
        "--host",
        default="0.0.0.0",
        help="Host to bind the server to (default: 0.0.0.0)",
    )

    parser.add_argument(
        "--no-reload", action="store_true", help="Disable auto-reload on code changes"
    )

    return parser.parse_args()


def main():
    """Main function to run the application."""
    args = parse_arguments()
    print_banner()

    # Check dependencies
    if not check_dependencies():
        sys.exit(1)

    # Setup backend
    if not setup_backend():
        sys.exit(1)

    # Start the server
    if not start_backend(args):
        sys.exit(1)

    print("\n✓ Application stopped successfully")


if __name__ == "__main__":
    main()
