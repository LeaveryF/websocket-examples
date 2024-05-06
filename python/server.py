#!/usr/bin/env python

import asyncio
import websockets

async def echo(websocket):
    message = await websocket.recv()
    print(f"<<< {message}")

    await websocket.send(message)
    print(f">>> {message}")

async def main():
    async with websockets.serve(echo, "localhost", 1234):
        await asyncio.Future()  # run forever

if __name__ == "__main__":
    asyncio.run(main())