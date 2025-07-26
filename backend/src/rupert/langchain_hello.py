"""LangChain integration for Rupert AI Assistant."""

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough


class LangChainHello:
    """Simple LangChain integration for Rupert."""
    
    def __init__(self):
        """Initialize the LangChain components."""
        # Create a simple prompt template
        self.prompt = ChatPromptTemplate.from_messages([
            ("system", "You are Rupert, a helpful AI assistant with personality. Always be friendly and helpful."),
            ("user", "{input}")
        ])
        
        # Create a simple chain (without LLM for now - just echo with formatting)
        self.chain = (
            {"input": RunnablePassthrough()}
            | self.prompt
            | self._mock_llm_response
        )
    
    def _mock_llm_response(self, messages):
        """Mock LLM response for testing without actual LLM."""
        # Extract user input
        user_message = messages.messages[-1].content
        
        # Generate a simple response
        if "yourself" in user_message.lower():
            return "Hello! I'm Rupert, your personal AI assistant. I'm here to help you with various tasks while maintaining a friendly and adaptive personality. I'm built with memory capabilities to remember our conversations and learn from our interactions."
        
        return f"Hi! I'm Rupert. You said: '{user_message}'. How can I assist you today?"
    
    def respond(self, user_input: str) -> str:
        """
        Generate a response to user input.
        
        Args:
            user_input: The user's message.
            
        Returns:
            The assistant's response.
        """
        return self.chain.invoke(user_input)