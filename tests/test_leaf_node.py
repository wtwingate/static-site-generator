import unittest
from src.leaf_node import LeafNode


class TestLeafNodeToHTML(unittest.TestCase):
    def test_to_html_plain_text(self):
        node = LeafNode(None, "howdy there!")
        self.assertEqual(node.to_html(), "howdy there!")

    def test_to_html_para(self):
        node = LeafNode("p", "this is a paragraph")
        self.assertEqual(node.to_html(), "<p>this is a paragraph</p>")

    def test_to_html_link(self):
        node = LeafNode("a", "click me!", {"href": "https://www.mallard.dev"})
        self.assertEqual(
            node.to_html(), '<a href="https://www.mallard.dev">click me!</a>'
        )

    def test_to_html_error(self):
        node = LeafNode("p", None)
        with self.assertRaises(ValueError):
            node.to_html()
