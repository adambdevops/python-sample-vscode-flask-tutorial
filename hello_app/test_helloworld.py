import unittest
from .helloworld import helloWorld

class TestHelloWorldMethods(unittest.TestCase):

    def test_helloworld(self):
        self.assertEqual(helloWorld.hello_world(self, "adam"), 'Hello adam')