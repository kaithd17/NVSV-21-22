import asyncio
import pathlib
import ssl
import websockets

#To make sure that the client will connect to secure WebSocket server
ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
localhost_pem = pathlib.Path(__file__).with_name("localhost.pem")
ssl_context.load_verify_locations(localhost_pem)

#async --> asynchronous method
#await --> is necessary if your method is an async method
async def hello():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri, ssl = ssl_context) as websocket:
        name = input("What's your name? ")

        await websocket.send(name)
        print(f">>> {name}")

        greeting = await websocket.recv()
        print(f"<<< {greeting}")

asyncio.run(hello())