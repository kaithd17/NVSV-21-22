import asyncio
import websockets

async def test():
    print("test")

async def main():
    async with websockets.serve(test, "localhost", 5678):
        await asyncio.Future()

asyncio.run(main())