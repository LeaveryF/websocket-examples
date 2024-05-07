#!/usr/bin/env python

import asyncio
import websockets

async def echo():
    uri = "ws://localhost:1234"
    async with websockets.connect(uri) as websocket:
        message = input("Input a string: ")

        await websocket.send(message)
        print(f">>> {message}")

        receive = await websocket.recv()
        print(f"<<< {receive}")

if __name__ == "__main__":
    asyncio.run(echo())