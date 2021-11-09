## Lernlogbuch

#### WebSockets

- async --> asynchronous method
- await --> is necessary if your method is an async method, so the method waits until it is needed

#### Server:

- Websockets.serve --> starts server

```python
async with websockets.serve(hello, "localhost", 8765, ssl = ssl_context):
```

- The server is running until someone stops it

````python
await asyncio.Future()
````

#### Client:

- We build a connection to the websocket

```python
async with websockets.connect(uri, ssl = ssl_context) as websocket
```

- Here we are sending data

```python
await websocket.send(data)
```

- We get a response from the sever

```py
greeting = await websocket.recv()
```

