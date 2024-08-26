# src/app.py
from message_store import Message, MessageStore
from conversation_manager import ConversationManager
from utils import log_info, format_timestamp
import asyncio
import websockets
from datetime import datetime

async def handle_client(websocket, path, message_store):
    async for message in websocket:
        msg_id = len(message_store.message_ids) + 1
        msg = Message(msg_id, message, datetime.now())
        message_store.add_message(1, msg)
        log_info(f"Message received and stored: {message}")
        await websocket.send(f"Message received and stored: {message}")

async def start_server(message_store):
    async with websockets.serve(lambda ws, path: handle_client(ws, path, message_store), "localhost", 8765):
        await asyncio.Future()

def main():
    # Initialize stores
    message_store = MessageStore()
    conv_manager = ConversationManager()

    # Example: Add conversations
    conv_manager.add_conversation(1, datetime.now())

    # Start WebSocket server
    log_info("Starting WebSocket server...")
    asyncio.run(start_server(message_store))

if __name__ == "__main__":
    main()
