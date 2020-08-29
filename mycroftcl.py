#!/bin/env python
import json
from websocket import create_connection  # type: ignore
import logging
import sys
import os

## var setup
MYCROFTCL_LOGGING = os.environ.get("MYCROFTCL_LOGGING", logging.WARN)
logging.basicConfig(level=MYCROFTCL_LOGGING)
local_file_path = os.path.dirname(os.path.realpath(__file__))
MYCROFT_ADDR = os.environ.get("MYCROFT_ADDR", "localhost")
MYCROFT_PORT = os.environ.get("MYCROFT_PORT", "8181")
MYCROFT_JSON_DIR = os.environ.get(
    "MYCROFT_JSON_DIR", f"{local_file_path}/mycroft-json-messages"
)
LANG = os.environ.get("LANG", "en-us")
logging.debug("ENV VARS SET:")
logging.debug(f"MYCROFT_ADDR = {MYCROFT_ADDR}")
logging.debug(f"MYCROFT_PORT = {MYCROFT_PORT}")
logging.debug(f"MYCROFT_JSON_DIR = {MYCROFT_JSON_DIR}")
logging.debug(f"LANG = {LANG}")


def send_message(message: dict, mycroft_addr=MYCROFT_ADDR, mycroft_port=MYCROFT_PORT):
    """Creates websocket address string, connects and sends fully formed json message"""
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


def get_mycroft_message(command: str, json_dir=MYCROFT_JSON_DIR) -> dict:
    """Retrives and loads the correct json file for the command given"""
    json_file = f"{json_dir}/{command}.json"
    logging.debug(f"json_file: {json_file}")
    with open(f"{json_file}", "rb") as fh:
        message = json.load(fh)
    logging.debug(f"json_message: {message}")
    return message


def run(command: str, data: list, mycroft_addr=MYCROFT_ADDR, mycroft_port=MYCROFT_PORT):
    """Parses data into expected json fields depending on which command is provided"""
    message = get_mycroft_message(command)
    if command == "speak":
        data_string = " ".join(data)
        message["data"]["utterance"] = data_string
    elif command == "say-to":
        message["data"]["utterances"] = data
        message["data"]["lang"] = LANG
    elif command == "question-query":
        data_string = " ".join(data)
        message["data"]["phrase"] = data_string
    send_message(message, mycroft_addr, mycroft_port)


if __name__ == "__main__":
    if sys.stdin.isatty():
        logging.debug(f"Passing args: {sys.argv[2:]}")
        run(sys.argv[1], sys.argv[2:])
    else:
        logging.debug("No args given defaulting to stdin")
        for line in sys.stdin:
            run(sys.argv[1], [line])
