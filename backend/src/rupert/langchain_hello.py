"""LangChain integration for Rupert AI Assistant."""

from typing import Optional, Any

from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough, Runnable

from rupert.llm import LLMProvider, LLMService


class LangChainHello:
    """Simple LangChain integration for Rupert."""

    def __init__(
        self, use_real_llm: bool = False, llm_provider: LLMProvider = LLMProvider.OPENAI
    ):
        """
        Initialize the LangChain components.

        Args:
            use_real_llm: Whether to use real LLM or mock response.
            llm_provider: Which LLM provider to use if use_real_llm is True.
        """
        self.use_real_llm = use_real_llm
        self.llm_service: Optional[LLMService] = None

        if use_real_llm:
            # Use real LLM service
            self.llm_service = LLMService(provider=llm_provider)
        else:
            # Create a simple prompt template for mock mode
            self.prompt = ChatPromptTemplate.from_messages(
                [
                    (
                        "system",
                        "You are Rupert, a helpful AI assistant with personality. Always be friendly and helpful.",
                    ),
                    ("user", "{input}"),
                ]
            )

            # Create a simple chain (without LLM for now - just echo with formatting)
            self.chain: Any = (
                {"input": RunnablePassthrough()} | self.prompt | self._mock_llm_response
            )

    def _mock_llm_response(self, messages):
        """Mock LLM response for testing without actual LLM."""
        # Extract user input
        user_message = messages.messages[-1].content

        # Generate a simple response
        if "yourself" in user_message.lower():
            return "Hello! I'm Rupert, your personal AI assistant. I'm here to help you with various tasks while maintaining a friendly and adaptive personality. I'm built with memory capabilities to remember our conversations and learn from our interactions."

        return (
            f"Hi! I'm Rupert. You said: '{user_message}'. How can I assist you today?"
        )

    def respond(self, user_input: str) -> str:
        """
        Generate a response to user input.

        Args:
            user_input: The user's message.

        Returns:
            The assistant's response.
        """
        if self.use_real_llm and self.llm_service:
            # Use real LLM service
            return self.llm_service.generate_response(user_input)
        else:
            # Use mock chain
            return self.chain.invoke(user_input)
