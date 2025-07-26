"""Main entry point for Rupert AI Assistant."""

from rupert.hello_world import HelloWorld
from rupert.langchain_hello import LangChainHello


def main():
    """Run the Hello World examples."""
    print("=" * 50)
    print("Welcome to Rupert AI Assistant!")
    print("=" * 50)
    
    # Basic Hello World
    hello = HelloWorld()
    print("\n1. Basic Hello World:")
    print(hello.greet())
    print(hello.greet("Friend"))
    
    # LangChain Hello
    langchain_hello = LangChainHello()
    print("\n2. LangChain Integration:")
    print(langchain_hello.respond("Tell me about yourself"))
    print()
    print(langchain_hello.respond("What's your purpose?"))
    
    print("\n" + "=" * 50)
    print("Rupert is ready for development!")
    print("=" * 50)


if __name__ == "__main__":
    main()