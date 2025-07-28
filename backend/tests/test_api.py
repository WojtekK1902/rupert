"""Tests for API endpoints following TDD principles."""

import pytest
from fastapi.testclient import TestClient
from rupert.api import app


@pytest.fixture
def client():
    """Create a test client for the API."""
    return TestClient(app)


def test_health_check_endpoint(client):
    """Test that health check endpoint returns 200 and proper response."""
    # Act
    response = client.get("/health")
    
    # Assert
    assert response.status_code == 200
    assert response.json() == {
        "status": "healthy",
        "service": "Rupert AI Assistant",
        "version": "0.1.0"
    }


def test_root_endpoint_redirects_to_docs(client):
    """Test that root endpoint redirects to API documentation."""
    # Act
    response = client.get("/", follow_redirects=False)
    
    # Assert
    assert response.status_code == 307
    assert response.headers["location"] == "/docs"


def test_chat_endpoint_exists(client):
    """Test that chat endpoint exists and accepts POST requests."""
    # Arrange
    chat_request = {
        "message": "Hello Rupert"
    }
    
    # Act
    response = client.post("/chat", json=chat_request)
    
    # Assert
    assert response.status_code == 200
    data = response.json()
    assert "response" in data
    assert isinstance(data["response"], str)
    assert len(data["response"]) > 0


def test_chat_endpoint_validates_input(client):
    """Test that chat endpoint validates input properly."""
    # Arrange
    invalid_request = {}
    
    # Act
    response = client.post("/chat", json=invalid_request)
    
    # Assert
    assert response.status_code == 422  # Unprocessable Entity


@pytest.mark.asyncio
async def test_chat_endpoint_handles_langchain():
    """Test that chat endpoint properly integrates with LangChain."""
    # This test will be implemented after basic structure is in place
    pass