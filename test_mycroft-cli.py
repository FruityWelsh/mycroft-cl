# /bin/env python3

import unittest
import websocket  # type: ignore
import mock
import mycroft_cl
import os


class test_speak_subcommand(unittest.TestCase):
    def setUp(self):
        self.MYCROFT_PORT_OLD = os.environ["MYCROFT_PORT"]
        self.MYCROFT_ADDR_OLD = os.environ["MYCROFT_ADDR"]
        os.environ["MYCROFT_PORT"] = "8181"
        os.environ["MYCROFT_ADDR"] = "localhost"

    def test_speak_subcommand(self):
        with unittest.mock.patch(mycroft_cl.create_connection):
            mycroft_cl.run("speak")

    def tearDown(self):
        os.environ["MYCROFT_PORT"] = self.MYCROFT_PORT_OLD
        os.environ["MYCROFT_ADDR"] = self.MYCROFT_ADDR_OLD
