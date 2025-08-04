"""Main entry point for Rupert AI Assistant."""

import uvicorn

from rupert.api import app


def main():
    """Run the Rupert API server."""
    print("=" * 50)
    print("Starting Rupert AI Assistant API")
    print("=" * 50)
    print("\nAPI Documentation: http://localhost:8000/docs")
    print("Health Check: http://localhost:8000/health")
    print("\nPress CTRL+C to stop the server")
    print("=" * 50)

    # Run the API server
    uvicorn.run(
        "rupert.api:app", host="0.0.0.0", port=8000, reload=True, log_level="info"
    )


if __name__ == "__main__":
    main()
