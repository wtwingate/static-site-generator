import unittest
from src.html_node import HTMLNode


class TestHTMLNodeToProps(unittest.TestCase):
    def test_empty_props(self):
        node = HTMLNode("p", "hello, world")
        self.assertEqual(node.props_to_html(), "")

    def test_single_props(self):
        node = HTMLNode(
            "a", "link", children=None, props={"href": "https://www.mallard.dev"}
        )
        self.assertEqual(node.props_to_html(), ' href="https://www.mallard.dev"')

    def test_multi_props(self):
        node = HTMLNode(
            "b",
            "pay attention",
            children=None,
            props={"class": "important", "id": "very-important"},
        )
        self.assertEqual(node.props_to_html(), ' class="important" id="very-important"')
