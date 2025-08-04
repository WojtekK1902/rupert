"""LLM service for real language model integration."""

import os
from enum import Enum
from typing import Optional

from langchain_anthropic import ChatAnthropic
from langchain_core.language_models import BaseChatModel
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import Runnable
from langchain_openai import ChatOpenAI
from pydantic import SecretStr


class LLMProvider(Enum):
    """Supported LLM providers."""

    OPENAI = "openai"
    ANTHROPIC = "anthropic"


class LLMService:
    """Service for interacting with language models."""

    def __init__(
        self,
        provider: LLMProvider = LLMProvider.OPENAI,
        model: Optional[str] = None,
        temperature: float = 0.7,
        system_prompt: Optional[str] = None,
    ):
        """
        Initialize LLM service.

        Args:
            provider: The LLM provider to use.
            model: The specific model to use (defaults to provider's default).
            temperature: The temperature for generation (0.0-1.0).
            system_prompt: Optional system prompt to use.

        Raises:
            ValueError: If API key is not found in environment.
        """
        self.provider = provider
        self.temperature = temperature
        self.system_prompt = (
            system_prompt
            or "You are Rupert, a helpful AI assistant with personality. Always be friendly and helpful."
        )
        
        # Type hint for llm
        self.llm: BaseChatModel

        # Initialize the LLM based on provider
        if provider == LLMProvider.OPENAI:
            api_key = os.getenv("OPENAI_API_KEY")
            if not api_key:
                raise ValueError(
                    "API key not found. Please set OPENAI_API_KEY environment variable."
                )

            self.llm = ChatOpenAI(
                api_key=SecretStr(api_key), model=model or "gpt-4o-mini", temperature=temperature
            )

        elif provider == LLMProvider.ANTHROPIC:
            api_key = os.getenv("ANTHROPIC_API_KEY")
            if not api_key:
                raise ValueError(
                    "API key not found. Please set ANTHROPIC_API_KEY environment variable."
                )

            self.llm = ChatAnthropic(
                api_key=SecretStr(api_key),
                model_name=model or "claude-3-haiku-20240307",
                temperature=temperature,
                timeout=60,
                stop=[],
            )

        else:
            raise ValueError(f"Unsupported provider: {provider}")

        # Create the prompt template
        self.prompt_template = ChatPromptTemplate.from_messages(
            [("system", self.system_prompt), ("user", "{input}")]
        )

        # Create the chain
        self.chain = self.prompt_template | self.llm | StrOutputParser()

    def generate_response(self, user_input: str) -> str:
        """
        Generate a response from the LLM.

        Args:
            user_input: The user's input message.

        Returns:
            The LLM's response.
        """
        return self.chain.invoke({"input": user_input})
