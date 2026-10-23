# Python Chapter 02: Local AI Assistant

A small Python application that runs a local AI assistant using Ollama and a local language model. This project is intended as a beginner-friendly example of building a chat interface that keeps a short memory of prior conversation and can answer questions from a local LLM.

## Features

- Local AI chat using Ollama
- Simple command-based CLI interface
- Conversation history support
- Clear and view chat history commands
- Lightweight setup for learning and experimentation

## Project files

- `main.py` - CLI entry point and chat loop
- `ollama_service.py` - wrapper for communicating with Ollama
- `chat_memory.py` - stores recent conversation history
- `settings.py` - model, prompts, and timeout configuration
- `requirements.txt` - Python dependencies

## Requirements

- Python 3.10+
- Ollama installed and running locally
- A downloaded local model such as `qwen3.5:9b`

## Setup

1. Install Python dependencies:

```bash
pip install -r requirements.txt
```

2. Start Ollama locally.

3. Make sure the model is available. For example:

```bash
ollama pull qwen3.5:9b
```

4. Run the application:

```bash
python main.py
```

## Usage

When the app starts, you can type questions directly into the terminal. Built-in commands include:

- `history` - view the conversation history
- `clear` - clear the current chat memory
- `help` - display the command list
- `exit` or `quit` - close the app

## Notes

This project is a learning example focused on:

- calling a local LLM through Ollama
- keeping a limited conversation history
- building a basic command-line AI assistant in Python

## Configuration

The main settings are defined in `settings.py`, including:

- `OLLAMA_HOST` - local Ollama server URL
- `MODEL_NAME` - the model to use
- `TIMEOUT_SECONDS` - request timeout duration
- `MAX_HISTORY_MESSAGES` - number of recent chat exchanges retained
- `SYSTEM_PROMPT` - instructions given to the assistant

## License

This project is provided for educational purposes.
