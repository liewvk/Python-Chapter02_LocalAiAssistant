# chat_memory.py

class ChatMemory:
    def __init__(self, max_messages=10):

        if max_messages < 1:
            raise ValueError(
                "max_messages must be greater than zero."
            )

        self.max_messages = max_messages
        self.history = []

    def add_exchange(self, user_text, assistant_text):
        """Save a user question and AI response."""

        self.history.append({
            "role": "user",
            "content": user_text
        })

        self.history.append({
            "role": "assistant",
            "content": assistant_text
        })

        # Keep only recent messages.
        self.history = self.history[
            -self.max_messages:
        ]

    def get_history(self):
        """Return a copy of recent messages."""

        return self.history.copy()

    def clear(self):
        """Delete conversation history."""

        self.history.clear()

    def display_history(self):
        """Display saved conversation messages."""

        if not self.history:
            print("No conversation history.")
            return

        print("\nConversation History")
        print("--------------------")

        for message in self.history:

            role = message["role"].capitalize()
            content = message["content"]

            print(f"\n{role}: {content}")

