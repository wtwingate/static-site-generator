from inline import split_nodes_delimiter
from inline import extract_markdown_images
from inline import extract_markdown_links
from textnode import TextNode
import unittest


class TestSplitNodesDelimiter(unittest.TestCase):
    def test_bold(self):
        old_nodes = [
            TextNode("Here is some **bold** text", "text"),
            TextNode("**SUCH BOLDNESS**", "text"),
            TextNode("Not very bold at all", "text"),
        ]
        self.assertEqual(
            split_nodes_delimiter(old_nodes, "**", "bold"),
            [
                TextNode("Here is some ", "text"),
                TextNode("bold", "bold"),
                TextNode(" text", "text"),
                TextNode("SUCH BOLDNESS", "bold"),
                TextNode("Not very bold at all", "text"),
            ],
        )

    def test_italic(self):
        old_nodes = [
            TextNode("Here is some *italic* text", "text"),
            TextNode("*Mama Mia! That's a spicy meat-a-ball!*", "text"),
            TextNode("Nothing to see here", "text"),
        ]
        self.assertEqual(
            split_nodes_delimiter(old_nodes, "*", "italic"),
            [
                TextNode("Here is some ", "text"),
                TextNode("italic", "italic"),
                TextNode(" text", "text"),
                TextNode("Mama Mia! That's a spicy meat-a-ball!", "italic"),
                TextNode("Nothing to see here", "text"),
            ],
        )

    def test_code(self):
        old_nodes = [
            TextNode("Here is some `code` text", "text"),
            TextNode("`print('hello, world')`", "text"),
            TextNode("I'm a luddite!", "text"),
        ]
        self.assertEqual(
            split_nodes_delimiter(old_nodes, "`", "code"),
            [
                TextNode("Here is some ", "text"),
                TextNode("code", "code"),
                TextNode(" text", "text"),
                TextNode("print('hello, world')", "code"),
                TextNode("I'm a luddite!", "text"),
            ],
        )

    def test_bad_syntax(self):
        old_nodes = [
            TextNode("Here is some invalid **bold text", "text"),
        ]
        with self.assertRaises(Exception):
            split_nodes_delimiter(old_nodes, "**", "bold")


class TestExtractMarkdown(unittest.TestCase):
    def test_extract_images(self):
        text = "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and ![another](https://i.imgur.com/dfsdkjfd.png)"
        self.assertEqual(
            extract_markdown_images(text),
            [
                ("image", "https://i.imgur.com/zjjcJKZ.png"),
                ("another", "https://i.imgur.com/dfsdkjfd.png"),
            ],
        )

    def test_extract_links(self):
        text = "This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)"
        self.assertEqual(
            extract_markdown_links(text),
            [
                ("link", "https://www.example.com"),
                ("another", "https://www.example.com/another"),
            ],
        )
