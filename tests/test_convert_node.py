import unittest
from src.convert_node import text_node_to_leaf_node
from src.text_node import TextNode
from src.leaf_node import LeafNode


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
