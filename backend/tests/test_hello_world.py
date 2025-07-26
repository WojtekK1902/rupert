"""Test for Hello World functionality following TDD principles."""

import pytest
from rupert.hello_world import HelloWorld


def test_hello_world_returns_greeting():
    """Test that HelloWorld returns the expected greeting."""
    # Arrange
    hello = HelloWorld()
    
    # Act
    result = hello.greet()
    
    # Assert
    assert result == "Hello, I'm Rupert, your AI assistant!"


def test_hello_world_personalized_greeting():
    """Test that HelloWorld can return a personalized greeting."""
    # Arrange
    hello = HelloWorld()
    name = "Wojciech"
    
    # Act
    result = hello.greet(name)
    
    # Assert
    assert result == f"Hello {name}, I'm Rupert, your AI assistant!"