import unittest
from node_markdown import *
from node_html import *
from node_text import *


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", text_type_bold, "https://www.boot.dev")
        node2 = TextNode("This is a text node", text_type_bold, "https://www.boot.dev")
        self.assertEqual(node, node2)

    def test_none(self):
        node = TextNode("This is a text node", text_type_bold, None)
        node2 = TextNode("This is a text node", text_type_bold, None)
        self.assertEqual(node, node2)

    def test_uneq1(self):
        node = TextNode("This is a text node", text_type_bold, "https://www.boot.dev")
        node2 = TextNode(
            "This is a different text node", text_type_bold, "https://www.boot.dev"
        )
        self.assertNotEqual(node, node2)

    def test_uneq2(self):
        node = TextNode("This is a text node", text_type_italic, "https://www.boot.dev")
        node2 = TextNode("This is a text node", text_type_bold, "https://www.boot.dev")
        self.assertNotEqual(node, node2)

    def test_uneq3(self):
        node = TextNode("This is a text node", text_type_bold, "https://www.boot.dev")
        node2 = TextNode(
            "This is a text node", text_type_bold, "https://www.boots_is_bae.dev"
        )
        self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()
