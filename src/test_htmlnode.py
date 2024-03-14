import unittest
from node_markdown import *
from node_html import *
from node_text import *


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html1(self):
        node = HTMLNode(
            "a",
            "Hello, World",
            None,
            {"href": "https://www.boot.dev", "target": "_blank"},
        )
        result = node.props_to_html()
        expected = ' href="https://www.boot.dev" target="_blank"'
        self.assertEqual(result, expected)

    def test_props_to_html2(self):
        node = HTMLNode("h1", "Howdy, Folks!", None, None)
        result = node.props_to_html()
        expected = ""
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
