"""Hello World module for Rupert AI Assistant."""

from typing import Optional


class HelloWorld:
    """Simple Hello World class for Rupert."""
    
    def greet(self, name: Optional[str] = None) -> str:
        """
        Return a greeting message.
        
        Args:
            name: Optional name to personalize the greeting.
            
        Returns:
            A greeting string.
        """
        if name:
            return f"Hello {name}, I'm Rupert, your AI assistant!"
        return "Hello, I'm Rupert, your AI assistant!"