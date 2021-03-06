#!/bin/env python3

import unittest
import websocket  # type: ignore
import mock
import mycroft_cl
import os


class test_speak_subcommand(unittest.TestCase):
    def setUp(self):
        self.MYCROFT_PORT_OLD = os.environ["MYCROFT_PORT"]
        self.MYCROFT_ADDR_OLD = os.environ["MYCROFT_ADDR"]
        self.MYCROFT_JSON_DIR = os.environ["MYCROFT_JSON_DIR"]
        os.environ["MYCROFT_PORT"] = "8181"
        os.environ["MYCROFT_ADDR"] = "localhost"
        os.environ["MYCROFT_JSON_DIR"] = "%s/mycroft-json-messages" % (
            os.path.dirname(os.path.realpath(__file__))
        )

    def test_speak_subcommand(self):
        with unittest.mock.patch(mycroft_cl.create_connection):
            mycroft_cl.run("speak", "hello")

    def test_listen_subcommand(self):
        with unittest.mock.patch(mycroft_cl.create_connection):
            mycroft_cl.run("listen")

    def tearDown(self):
        os.environ["MYCROFT_PORT"] = self.MYCROFT_PORT_OLD
        os.environ["MYCROFT_ADDR"] = self.MYCROFT_ADDR_OLD
