# Rupert AI Assistant - Project Guide

## Project Overview
This is a deeply personal AI assistant project called "Rupert" - an assistant with memory, personality, and purpose.

## Core Philosophy
- **Personal & Adaptive**: Building an assistant that understands and adapts to individual needs
- **Memory-Driven**: Persistent memory across conversations and interactions
- **Personality-First**: Not just functional, but genuinely personable

## IMPORTANT Guidelines
- **YOU MUST** follow TDD for all new features and components - write failing tests before any implementation code
- **YOU MUST** use Poetry for all dependency management - never use pip directly
- **YOU MUST** use Python 3.12 for development
- **ALWAYS** commit poetry.lock file to ensure reproducible builds
- **YOU MUST** use LangChain as a framework for building LLM-powered applications. When in doubt, refer to the [LangChain documentation](https://python.langchain.com/docs/tutorials/).
- **NEVER** commit API keys or sensitive data

## TDD Workflow
1. Red: Write a failing test first
2. Green: Write minimal code to make it pass
3. Refactor: Improve code while keeping tests green
4. Repeat: Continue for each small feature increment

## Code Style Guidelines
- **Python Style**: Follow PEP 8 with Black formatting
- **Type Hints**: Use type hints for all public functions and class methods
- **Docstrings**: Use Google-style docstrings for all modules, classes, and functions
- **Import Style**: Use absolute imports, sort with isort
- **LangChain Patterns**: Follow LangChain best practices for LLM-powered applications

## Project Structure
```
rupert/
├── backend/            # Backend code
│   ├── src/
│   │   └── rupert/     # Main package (importable as 'rupert')
│   └── tests/          # Tests mirror src structure
├── docs/               # Documentation
├── pyproject.toml      # Poetry configuration
└── poetry.lock         # Locked dependencies
```

## Testing Guidelines
* **YOU MUST** use pytest framework for all testing
* Follow the AAA Pattern for all tests:
  * Arrange: Set up test data and conditions
  * Act: Execute the function/method being tested
  * Assert: Verify the expected outcome
* Naming convention:
  * Test files: test_*.py or *_test.py
  * Test functions: test_[what]_[when]_[expected]()

## Development Workflow
1. **Plan**: Have Claude create implementation plans before coding
2. **Test scenarios**: Write test scenarios before implementation
3. **Red-Green-Refactor**: Implement minimal code to pass tests, then refactor
4. **Test & Verify**: Ensure all tests pass and coverage is maintained
5. **Document**: Update docs and commit changes
6. **Iterate**: Refine based on testing and usage

## Git Workflow
- **Branch Naming**: `feature/memory-improvements`, `fix/conversation-bug`
- **Commit Style**: Conventional commits (feat:, fix:, docs:, etc.)
- **Before Committing**: Run tests
- **After Committing**: Push changes and create a PR

## Common Commands

### Running the Application
```bash
# Run the main application
poetry run python -m rupert.main

# Run specific modules
poetry run python -m rupert.hello_world
```

### Testing
```bash
# Run all tests
poetry run pytest

# Run tests with verbose output
poetry run pytest -v

# Run specific test file
poetry run pytest tests/test_hello_world.py

# Run tests with coverage
poetry run pytest --cov=rupert --cov-report=html
```

### Code Quality
```bash
# Run quality checks (code formatting, imports sorting, type checking)
poetry run black src tests && poetry run isort src tests && poetry run mypy src
```

## Documentation
- Keep this CLAUDE.md updated as the project evolves
- Document new features, integrations and their capabilities
