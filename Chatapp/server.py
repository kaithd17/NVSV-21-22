import asyncio
import websockets
import json

USERS = set()

#This function builds a message with the current amount of users and if a user (=username) joined or left the chat (=action)
def users_event(action, username):
    return json.dumps({
        "type":"users",
        "username":username,
        "count":len(USERS),
        "action":action
    })

#This function adds a user and it sends a message with this information to all users
def add_user(websocket, username):
    USERS.add(websocket)
    websockets.broadcast(USERS, users_event("addUser", username))

#This function removes a user and it sends a message with this information to all users
def remove_user(websocket, username):
    USERS.remove(websocket)
    websockets.broadcast(USERS, users_event("removeUser", username))

#This function builds a message with the user who sent a message and it includes the message itself
def message_event(data):
    return json.dumps({
        "type":"message",
        "username":data["username"],
        "message":data["message"]
    })

#This function sends the message to all users
def send_message(data):
    websockets.broadcast(USERS, message_event(data))

#This function handles all requests which are coming from the users
async def message_handler(websocket, path):
    try:
        async for message in websocket:
            data = json.loads(message)
            if data["action"] == "newUser":
                add_user(websocket, data["username"])
            elif data["action"] == "newMessage":
                send_message(data)
    finally:
        remove_user(websocket, data["username"])

async def main():
    async with websockets.serve(message_handler, "localhost", 5678):
        await asyncio.Future()

asyncio.run(main())