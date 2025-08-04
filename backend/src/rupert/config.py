"""Configuration for Rupert AI Assistant."""

import os
from enum import Enum
from typing import Optional

from dotenv import load_dotenv

from rupert.llm import LLMProvider

# Load environment variables from .env file
load_dotenv()


class Config:
    """Configuration settings for Rupert."""

    def __init__(self):
        """Initialize configuration from environment variables."""
        self.use_real_llm = os.getenv("USE_REAL_LLM", "false").lower() == "true"

        # LLM provider configuration
        provider_str = os.getenv("LLM_PROVIDER", "openai").lower()
        if provider_str == "anthropic":
            self.llm_provider = LLMProvider.ANTHROPIC
        else:
            self.llm_provider = LLMProvider.OPENAI

        # API keys (will be read by LLMService when needed)
        self.openai_api_key = os.getenv("OPENAI_API_KEY")
        self.anthropic_api_key = os.getenv("ANTHROPIC_API_KEY")

    def validate(self) -> None:
        """
        Validate configuration.

        Raises:
            ValueError: If configuration is invalid.
        """
        if self.use_real_llm:
            if self.llm_provider == LLMProvider.OPENAI and not self.openai_api_key:
                raise ValueError(
                    "OPENAI_API_KEY environment variable is required when using OpenAI provider"
                )
            elif (
                self.llm_provider == LLMProvider.ANTHROPIC
                and not self.anthropic_api_key
            ):
                raise ValueError(
                    "ANTHROPIC_API_KEY environment variable is required when using Anthropic provider"
                )


# Global configuration instance
config = Config()
