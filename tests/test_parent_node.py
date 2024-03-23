import unittest
from src.parent_node import ParentNode
from src.leaf_node import LeafNode


class TestParentNodeToHTML(unittest.TestCase):
    def test_to_html_flat(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "bold text"),
                LeafNode(None, "normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>bold text</b>normal text<i>italic text</i>normal text</p>",
        )

    def test_to_html_nested(self):
        node = ParentNode(
            "div",
            [
                ParentNode("p", [LeafNode("b", "nested bold text")]),
                ParentNode("p", [LeafNode("i", "nested italic text")]),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<div><p><b>nested bold text</b></p><p><i>nested italic text</i></p></div>",
        )

    def test_to_html_with_props(self):
        node = ParentNode(
            "div",
            [LeafNode("a", "click me!", {"href": "https://www.mallard.dev"})],
            {"class": "links"},
        )
        self.assertEqual(
            node.to_html(),
            '<div class="links"><a href="https://www.mallard.dev">click me!</a></div>',
        )

    def test_to_html_no_tag(self):
        node = ParentNode(None, [LeafNode(None, "plain text")])
        with self.assertRaises(ValueError):
            node.to_html()

    def test_to_html_no_children(self):
        node = ParentNode("div", None)
        with self.assertRaises(ValueError):
            node.to_html()
