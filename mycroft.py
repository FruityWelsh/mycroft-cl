#!/bin/env python
import json
from websocket import create_connection  # type: ignore

with open("./mycroft-json-messages/listen.json", "rb") as fh:
    listen = json.load(fh)

mycroft_address = "localhost"
mycroft_port = "8181"

url = f"ws://{mycroft_address}:{mycroft_port}/core"
ws = create_connection(url)
# try
print(f"String sent: {listen}")
send_status = ws.send(json.dumps(listen))
print(f"Send status: {send_status}")
result = ws.recv()
print(f"received: {result}")
# except:
print("Failed")
ws.close()
