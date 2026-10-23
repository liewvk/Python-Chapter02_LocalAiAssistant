# main.py

from ollama import ResponseError

from httpx import (
    ConnectError,
    ConnectTimeout,
    ReadTimeout
)

from settings import (
    MODEL_NAME,
    SYSTEM_PROMPT,
    MAX_HISTORY_MESSAGES
)

from ollama_service import OllamaService
from chat_memory import ChatMemory


def display_header():

    print("========================================")
    print("     PYTHON LOCAL AI ASSISTANT")
    print("     Visual Studio 2026")
    print("     Ollama + Qwen 3.5")
    print("========================================")

    print(f"Model: {MODEL_NAME}")
    print()
    print("Commands:")
    print("  history - View conversation")
    print("  clear   - Clear conversation")
    print("  help    - Show commands")
    print("  exit    - Close the application")


def main():

    # Create application services.
    ai_service = OllamaService()

    memory = ChatMemory(
        MAX_HISTORY_MESSAGES
    )

    display_header()

    while True:

        print()
        question = input("You: ").strip()

        if not question:
            print("Please enter a question.")
            continue

        command = question.lower()

        if command in ("exit", "quit"):
            print("Goodbye!")
            break

        if command == "help":
            display_header()
            continue

        if command == "history":
            memory.display_history()
            continue

        if command == "clear":
            memory.clear()

            print(
                "Conversation history has been cleared."
            )
            continue

        # Prepare conversation messages.
        messages = [
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            }
        ]

        # Add recent conversation history.
        messages.extend(
            memory.get_history()
        )

        # Add the current user question.
        messages.append({
            "role": "user",
            "content": question
        })

        print("\nGenerating response...")

        try:

            # Send messages to Qwen 3.5.
            answer = ai_service.ask(messages)

            print("\nAssistant:")
            print(answer)

            # Save the successful exchange.
            memory.add_exchange(
                question,
                answer
            )

        except ResponseError as ex:

            print("\nOllama returned an error:")
            print(ex)

            print(
                "Check that the selected model "
                "is installed."
            )

        except (ConnectError, ConnectTimeout):

            print("\nCannot connect to Ollama.")

            print(
                "Ensure the Ollama server "
                "is running at localhost:11434."
            )

        except ReadTimeout:

            print(
                "\nThe AI request timed out."
            )

            print(
                "The model may require more "
                "time or computing resources."
            )

        except Exception as ex:

            print("\nUnexpected error:")
            print(ex)


if __name__ == "__main__":main()

