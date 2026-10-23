# ollama_service.py

from ollama import Client

from settings import (
    OLLAMA_HOST,
    MODEL_NAME,
    TIMEOUT_SECONDS
)


class OllamaService:

    def __init__(self):

        self.client = Client(
            host=OLLAMA_HOST,
            timeout=TIMEOUT_SECONDS
        )

        self.model = MODEL_NAME

    def ask(self, messages):
        """Send conversation messages to Ollama."""

        response = self.client.chat(
            model=self.model,
            messages=messages,
            stream=False,
            think=False,
            options={
                "temperature": 0.3,
                "num_predict": 300
            }
        )

        answer = response.message.content

        if not answer or not answer.strip():
            raise ValueError(
                "Ollama returned an empty response."
            )

        return answer.strip()

