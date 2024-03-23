import unittest
from src.constants import *
from src.convert_node import split_nodes_image, text_node_to_leaf_node
from src.convert_node import split_nodes_delimiter
from src.convert_node import split_nodes_link
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


class TestSplitNodesDelimiter(unittest.TestCase):
    def test_split_plain_text(self):
        old_nodes = [TextNode("normal text", "text")]
        new_nodes = [TextNode("normal text", "text")]
        self.assertEqual(
            split_nodes_delimiter(old_nodes, "**", TEXT_TYPE_BOLD), new_nodes
        )

    def test_split_bold_text(self):
        old_nodes = [TextNode("here is some **bold** text", "text")]
        new_nodes = [
            TextNode("here is some ", "text"),
            TextNode("bold", "bold"),
            TextNode(" text", "text"),
        ]
        self.assertEqual(
            split_nodes_delimiter(old_nodes, "**", TEXT_TYPE_BOLD), new_nodes
        )

    def test_split_italic_text(self):
        old_nodes = [TextNode("here is some *italic* text", "text")]
        new_nodes = [
            TextNode("here is some ", "text"),
            TextNode("italic", "italic"),
            TextNode(" text", "text"),
        ]
        self.assertEqual(
            split_nodes_delimiter(old_nodes, "*", TEXT_TYPE_ITALIC), new_nodes
        )

    def test_split_code_text(self):
        old_nodes = [TextNode("here is some `code` text", "text")]
        new_nodes = [
            TextNode("here is some ", "text"),
            TextNode("code", "code"),
            TextNode(" text", "text"),
        ]
        self.assertEqual(
            split_nodes_delimiter(old_nodes, "`", TEXT_TYPE_CODE), new_nodes
        )

    def test_split_multiple(self):
        old_nodes = [TextNode("**Behold!** Here is some **bold text!**", "text")]
        new_nodes = [
            TextNode("Behold!", "bold"),
            TextNode(" Here is some ", "text"),
            TextNode("bold text!", "bold"),
        ]
        self.assertEqual(
            split_nodes_delimiter(old_nodes, "**", TEXT_TYPE_BOLD), new_nodes
        )

    def test_split_error(self):
        old_nodes = [TextNode("invalid **bold text", "text")]
        with self.assertRaises(Exception):
            split_nodes_delimiter(old_nodes, "**", TEXT_TYPE_BOLD)


class TestSplitNodesLinkImage(unittest.TestCase):
    def test_split_nodes_link(self):
        old_nodes = [
            TextNode(
                "Follow me on [Twitter](https://twitter.com/wtwingate) and [GitHub](https://github.com/wtwingate)",
                "text",
            )
        ]
        new_nodes = [
            TextNode("Follow me on ", "text"),
            TextNode("Twitter", "link", "https://twitter.com/wtwingate"),
            TextNode(" and ", "text"),
            TextNode("GitHub", "link", "https://github.com/wtwingate"),
        ]
        self.assertEqual(split_nodes_link(old_nodes), new_nodes)

    def test_split_nodes_image(self):
        old_nodes = [
            TextNode(
                "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
                "text",
            )
        ]
        new_nodes = [
            TextNode("This is text with an ", "text"),
            TextNode("image", "image", "https://i.imgur.com/zjjcJKZ.png"),
            TextNode(" and another ", "text"),
            TextNode("second image", "image", "https://i.imgur.com/3elNhQu.png"),
        ]
        self.assertEqual(split_nodes_image(old_nodes), new_nodes)
