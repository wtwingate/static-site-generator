import unittest
from src.text_node import TextNode


class TestTextNodeEqual(unittest.TestCase):
    def test_equal(self):
        textnode1 = TextNode("Sample text", "bold", "https://www.mallard.dev")
        textnode2 = TextNode("Sample text", "bold", "https://www.mallard.dev")
        self.assertEqual(textnode1, textnode2)

    def test_unequal(self):
        textnode1 = TextNode("Sample text", "bold", "https://www.mallard.dev")
        textnode2 = TextNode("Different text", "italic", "https://www.example.com")
        self.assertNotEqual(textnode1, textnode2)
