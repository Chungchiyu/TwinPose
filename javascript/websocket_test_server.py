import asyncio
import websockets
import json

async def handle(ws):
    print("Client connected")

    try:
        async for message in ws:
            print("Received:", message)

            # 如果是 JSON，回傳 JSON
            try:
                data = json.loads(message)
            except:
                data = {"received": message}

            await ws.send(json.dumps({
                "status": "ok",
                "echo": data
            }))
    except websockets.exceptions.ConnectionClosed:
        print("Client disconnected")

async def main():
    server = await websockets.serve(handle, "0.0.0.0", 8080)
    print("WebSocket Server running on ws://localhost:8080")
    await server.wait_closed()

asyncio.run(main())
