import unittest
from src.leaf_node import LeafNode, text_node_to_leaf_node
from src.text_node import TextNode


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


class TestTextNodeToLeafNode(unittest.TestCase):
    def test_text_to_leaf(self):
        text_node = TextNode("normal text", "text")
        leaf_node = LeafNode(None, "normal text")
        self.assertEqual(text_node_to_leaf_node(text_node), leaf_node)

    def test_bold_to_leaf(self):
        text_node = TextNode("bold text", "bold")
        leaf_node = LeafNode("b", "bold text")
        self.assertEqual(text_node_to_leaf_node(text_node), leaf_node)

    def test_italic_to_leaf(self):
        text_node = TextNode("italic text", "italic")
        leaf_node = LeafNode("i", "italic text")
        self.assertEqual(text_node_to_leaf_node(text_node), leaf_node)

    def test_code_to_leaf(self):
        text_node = TextNode("code text", "code")
        leaf_node = LeafNode("code", "code text")
        self.assertEqual(text_node_to_leaf_node(text_node), leaf_node)

    def test_link_to_leaf(self):
        text_node = TextNode("link text", "link", "https://www.mallard.dev")
        leaf_node = LeafNode("a", "link text", {"href": "https://www.mallard.dev"})
        self.assertEqual(text_node_to_leaf_node(text_node), leaf_node)

    def test_image_to_leaf(self):
        text_node = TextNode("image text", "image", "../images/duck.jpeg")
        leaf_node = LeafNode(
            "img", "", {"src": "../images/duck.jpeg", "alt": "image text"}
        )
        self.assertEqual(text_node_to_leaf_node(text_node), leaf_node)
