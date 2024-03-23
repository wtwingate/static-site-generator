import pytest
from src.html_node import HTMLNode


class TestHTMLNodeToProps:
    def test_empty_props(self):
        node = HTMLNode("p", "hello, world")
        assert node.props_to_html() == ""

    def test_single_props(self):
        node = HTMLNode(
            "a", "link", children=None, props={"href": "https://www.mallard.dev"}
        )
        assert node.props_to_html() == ' href="https://www.mallard.dev"'

    def test_multi_props(self):
        node = HTMLNode(
            "b",
            "pay attention",
            children=None,
            props={"class": "important", "id": "very-important"},
        )
        assert node.props_to_html() == ' class="important" id="very-important"'
