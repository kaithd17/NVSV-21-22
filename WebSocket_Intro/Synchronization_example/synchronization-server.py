import asyncio
import json
import logging
import websockets

logging.basicConfig()

STATE = {"value":0}

USERS = set()

def state_event():
    return json.dumps({"type":"state", **STATE})

def users_event():
    return json.dumps({"type":"users", "count": len(USERS)})

