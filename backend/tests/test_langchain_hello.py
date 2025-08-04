"""Test for LangChain integration following TDD principles."""

import pytest

from rupert.langchain_hello import LangChainHello


def test_langchain_hello_initialization():
    """Test that LangChainHello can be initialized."""
    # Arrange & Act
    hello = LangChainHello()

    # Assert
    assert hello is not None
    assert hasattr(hello, "chain")


def test_langchain_hello_generates_response():
    """Test that LangChainHello generates a response using LangChain."""
    # Arrange
    hello = LangChainHello()
    user_input = "Tell me about yourself"

    # Act
    response = hello.respond(user_input)

    # Assert
    assert isinstance(response, str)
    assert len(response) > 0
    assert "Rupert" in response
