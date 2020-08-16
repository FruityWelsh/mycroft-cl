#!/bin/env python
import json
from websocket import create_connection  # type: ignore
import logging
import sys
import os

logging.basicConfig(level=logging.DEBUG)
local_file_path = os.path.dirname(os.path.realpath(__file__))
MYCROFT_ADDR = os.environ.get("MYCROFT_ADDR", "localhost")
MYCROFT_PORT = os.environ.get("MYCROFT_PORT", "8181")
MYCROFT_JSON_DIR = os.environ.get(
    "MYCROFT_JSON_DIR", f"{local_file_path}/mycroft-json-messages"
)
logging.debug("ENV VARS SET:")
logging.debug(f"MYCROFT_ADDR = {MYCROFT_ADDR}")
logging.debug(f"MYCROFT_PORT = {MYCROFT_PORT}")
logging.debug(f"MYCROFT_JSON_DIR = {MYCROFT_JSON_DIR}")


def send_message(message, mycroft_addr=MYCROFT_ADDR, mycroft_port=MYCROFT_PORT):
    url = f"ws://{mycroft_addr}:{mycroft_port}/core"
    logging.debug(f"Websocket url: {url}")
    ws = create_connection(url)
    try:
        logging.debug(f"String sent: {message}")
        send_status = ws.send(json.dumps(message))
        logging.debug(f"Send status: {send_status}")
        result = ws.recv()
        logging.debug(f"received: {result}")
    finally:
        ws.close()


def get_mycroft_message(command, json_dir=MYCROFT_JSON_DIR):
    json_file = f"{json_dir}/{command}.json"
    logging.debug(f"json_file: {json_file}")
    with open(f"{json_file}", "rb") as fh:
        message = json.load(fh)
    logging.debug(f"json_message: {message}")
    return message


def run(command, data, mycroft_addr=MYCROFT_ADDR, mycroft_port=MYCROFT_PORT):
    message = get_mycroft_message(command)
    if command == "speak":
        message["data"]["utterance"] = "".join(data)
    send_message(message, mycroft_addr, mycroft_port)


if __name__ == "__main__":
    run(sys.argv[1], sys.argv[2:])
