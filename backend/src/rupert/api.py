"""FastAPI application for Rupert AI Assistant."""

from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse
from pydantic import BaseModel
from typing import Dict

from rupert import __version__
from rupert.langchain_hello import LangChainHello


app = FastAPI(
    title="Rupert AI Assistant",
    description="A personal AI assistant with memory and personality",
    version=__version__,
)


class ChatRequest(BaseModel):
    """Request model for chat endpoint."""
    message: str


class ChatResponse(BaseModel):
    """Response model for chat endpoint."""
    response: str


@app.get("/")
async def root():
    """Redirect root to API documentation."""
    return RedirectResponse(url="/docs", status_code=307)


@app.get("/health")
async def health_check() -> Dict[str, str]:
    """Health check endpoint."""
    return {
        "status": "healthy",
        "service": "Rupert AI Assistant",
        "version": __version__
    }


@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest) -> ChatResponse:
    """
    Chat with Rupert AI Assistant.
    
    Args:
        request: Chat request containing user message.
        
    Returns:
        Chat response from Rupert.
    """
    try:
        # Initialize LangChain hello (will be replaced with full assistant later)
        assistant = LangChainHello()
        
        # Get response
        response = assistant.respond(request.message)
        
        return ChatResponse(response=response)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))