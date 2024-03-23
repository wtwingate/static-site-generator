import pytest
from src.leaf_node import LeafNode


class TestLeafNodeToHTML:
    def test_to_html_plain_text(self):
        node = LeafNode(None, "howdy there!")
        assert node.to_html() == "howdy there!"

    def test_to_html_para(self):
        node = LeafNode("p", "this is a paragraph")
        assert node.to_html() == "<p>this is a paragraph</p>"

    def test_to_html_link(self):
        node = LeafNode("a", "click me!", {"href": "https://www.mallard.dev"})
        assert node.to_html() == '<a href="https://www.mallard.dev">click me!</a>'
