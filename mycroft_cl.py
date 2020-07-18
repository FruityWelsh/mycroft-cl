#!/bin/env python
import json
from websocket import create_connection  # type: ignore
import logging
import sys
import os

logging.basicConfig(level=logging.DEBUG)
try:
    MYCROFT_ADDR_ENV = os.environ["MYCROFT_ADDR"]
    MYCROFT_PORT_ENV = os.environ["MYCROFT_PORT"]
    JSON_DIR_ENV = os.environ["MYCROFT_JSON_DIR"]
    logging.info("ENV VARS SET")
except KeyError:
    logging.warning("ENV VARS NOT SET. Using default.")
    MYCROFT_ADDR_ENV = "localhost"
    MYCROFT_PORT_ENV = "8181"
    JSON_DIR_ENV = "%s/mycroft-json-messages" % (
        os.path.dirname(os.path.realpath(__file__))
    )


def send_message(message, mycroft_addr=MYCROFT_ADDR_ENV, mycroft_port=MYCROFT_PORT_ENV):
    url = f"ws://{mycroft_addr}:{mycroft_port}/core"
    logging.info(f"Websocket url: {url}")
    ws = create_connection(url)
    # try
    logging.info(f"String sent: {message}")
    send_status = ws.send(json.dumps(message))
    logging.info(f"Send status: {send_status}")
    result = ws.recv()
    logging.info(f"received: {result}")
    # except:
    logging.warning("Failed")
    ws.close()


def get_mycroft_message(command, json_dir=JSON_DIR_ENV):
    json_file = f"{json_dir}/{command}.json"
    logging.debug(f"json_file: {json_file}")
    with open(f"{json_file}", "rb") as fh:
        message = json.load(fh)
    logging.debug(f"json_message: {message}")
    return message


def run(command, data, mycroft_addr=MYCROFT_ADDR_ENV, mycroft_port=MYCROFT_PORT_ENV):
    message = get_mycroft_message(command)
    if command == "speak":
        message["data"]["utterance"] = "".join(data)
    send_message(message, mycroft_addr, mycroft_port)


if __name__ == "__main__":
    run(sys.argv[1], sys.argv[2:])
