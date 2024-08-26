# src/real_time_updates.py
import asyncio
import websockets

async def handle_client(websocket, path):
    async for message in websocket:
        # Echo the message back to the client (for demonstration purposes)
        await websocket.send(f"Message received: {message}")

async def start_server():
    async with websockets.serve(handle_client, "localhost", 8765):
        await asyncio.Future()  # Run until interrupted

# To run the WebSocket server, execute this script
if __name__ == "__main__":
    asyncio.run(start_server())
