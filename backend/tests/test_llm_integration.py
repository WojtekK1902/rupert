"""Test for real LLM integration following TDD principles."""

import os
from unittest.mock import MagicMock, patch

import pytest

from rupert.llm import LLMProvider, LLMService


def test_llm_module_exists():
    """Test that LLM module can be imported."""
    # This test will pass when we create the module
    assert LLMService is not None
    assert LLMProvider is not None


class TestLLMService:
    """Test suite for LLM service."""

    def test_llm_service_initialization_with_openai(self):
        """Test that LLMService can be initialized with OpenAI provider."""
        # Arrange
        with patch.dict(os.environ, {"OPENAI_API_KEY": "test-key"}):
            # Act
            service = LLMService(provider=LLMProvider.OPENAI)

            # Assert
            assert service is not None
            assert service.provider == LLMProvider.OPENAI
            assert service.llm is not None

    def test_llm_service_initialization_with_anthropic(self):
        """Test that LLMService can be initialized with Anthropic provider."""
        # Arrange
        with patch.dict(os.environ, {"ANTHROPIC_API_KEY": "test-key"}):
            # Act
            service = LLMService(provider=LLMProvider.ANTHROPIC)

            # Assert
            assert service is not None
            assert service.provider == LLMProvider.ANTHROPIC
            assert service.llm is not None

    def test_llm_service_raises_error_without_api_key(self):
        """Test that LLMService raises error when API key is missing."""
        # Arrange
        with patch.dict(os.environ, {}, clear=True):

            # Act & Assert
            with pytest.raises(ValueError, match="API key not found"):
                LLMService(provider=LLMProvider.OPENAI)

    def test_llm_service_generates_response(self):
        """Test that LLMService generates a response from LLM."""
        # Arrange
        expected_response = "Hello! I'm Rupert, your AI assistant."

        # Mock all the components before creating the service
        with patch.dict(os.environ, {"OPENAI_API_KEY": "test-key"}):
            with patch("rupert.llm.ChatOpenAI") as mock_chat, patch(
                "rupert.llm.ChatPromptTemplate"
            ) as mock_prompt, patch("rupert.llm.StrOutputParser") as mock_parser:

                # Setup mock LLM
                mock_llm_instance = MagicMock()
                mock_chat.return_value = mock_llm_instance

                # Setup mock prompt template
                mock_prompt_instance = MagicMock()
                mock_prompt.from_messages.return_value = mock_prompt_instance

                # Setup mock parser
                mock_parser_instance = MagicMock()
                mock_parser.return_value = mock_parser_instance

                # Setup mock chain (the | operator creates a chain)
                mock_chain = MagicMock()
                mock_prompt_instance.__or__ = MagicMock(return_value=mock_chain)
                mock_chain.__or__ = MagicMock(return_value=mock_chain)
                mock_chain.invoke.return_value = expected_response

                # Create service which will use our mocked components
                service = LLMService(provider=LLMProvider.OPENAI)

                # Act
                response = service.generate_response("Hello")

                # Assert
                assert isinstance(response, str)
                assert response == expected_response
                assert "Rupert" in response
                assert len(response) > 0

    def test_llm_service_with_system_prompt(self):
        """Test that LLMService uses system prompt correctly."""
        # Arrange
        system_prompt = "You are Rupert, a helpful AI assistant with personality."
        with patch.dict(os.environ, {"OPENAI_API_KEY": "test-key"}):
            service = LLMService(
                provider=LLMProvider.OPENAI, system_prompt=system_prompt
            )

            # Act & Assert
            assert service.system_prompt == system_prompt


class TestLangChainIntegration:
    """Test suite for LangChain integration with real LLM."""

    def test_langchain_hello_with_real_llm(self):
        """Test that LangChainHello can use real LLM service."""
        from rupert.langchain_hello import LangChainHello

        # Arrange
        expected_response = "Hello from real LLM!"

        with patch.dict(os.environ, {"OPENAI_API_KEY": "test-key"}):
            # Mock the LLMService
            with patch("rupert.langchain_hello.LLMService") as mock_llm_class:
                mock_service = MagicMock()
                mock_service.generate_response.return_value = expected_response
                mock_llm_class.return_value = mock_service

                # Act
                hello = LangChainHello(use_real_llm=True)
                response = hello.respond("Hello")

                # Assert
                assert response == expected_response
                mock_service.generate_response.assert_called_once_with("Hello")

    def test_langchain_hello_defaults_to_mock(self):
        """Test that LangChainHello defaults to mock when no LLM specified."""
        from rupert.langchain_hello import LangChainHello

        # Arrange
        hello = LangChainHello()

        # Act
        response = hello.respond("Tell me about yourself")

        # Assert
        assert "Rupert" in response
        assert isinstance(response, str)
