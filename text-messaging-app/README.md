# Text Messaging App

## Overview

This project is a demonstration of optimizing a text messaging app with efficient data structures for message storage, retrieval, and real-time updates.

## Project Structure

- `message_store.py`: Handles message storage and retrieval.
- `real_time_updates.py`: Implements WebSocket communication for real-time updates.
- `conversation_manager.py`: Manages conversations and provides sorting/filtering functionalities.
- `main.py`: Demonstrates the usage of the above modules.

## Requirements

- Python 3.x
- `websockets` library

## Installation

1. Clone the repository.
2. Install the requirements: `pip install -r requirements.txt`
3. Run the application: `python src/main.py`

To start the WebSocket server, run: `python src/real_time_updates.py`
