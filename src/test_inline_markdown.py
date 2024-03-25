import unittest
from constants import *
from inline_markdown import *
from text_node import TextNode


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


class TestExtractMarkdown(unittest.TestCase):
    def test_extract_links(self):
        text = "This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)"
        self.assertEqual(
            extract_markdown_links(text),
            [
                ("link", "https://www.example.com"),
                ("another", "https://www.example.com/another"),
            ],
        )

    def test_extract_images(self):
        text = "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and ![another](https://i.imgur.com/dfsdkjfd.png)"
        self.assertEqual(
            extract_markdown_images(text),
            [
                ("image", "https://i.imgur.com/zjjcJKZ.png"),
                ("another", "https://i.imgur.com/dfsdkjfd.png"),
            ],
        )


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


class TestMarkdownToTextNodes(unittest.TestCase):
    def test_markdown_to_text_nodes(self):
        text = "This is **text** with an *italic* word and a `code block` and an ![image](https://i.imgur.com/zjjcJKZ.png) and a [link](https://boot.dev)"
        text_nodes = [
            TextNode("This is ", TEXT_TYPE_TEXT),
            TextNode("text", TEXT_TYPE_BOLD),
            TextNode(" with an ", TEXT_TYPE_TEXT),
            TextNode("italic", TEXT_TYPE_ITALIC),
            TextNode(" word and a ", TEXT_TYPE_TEXT),
            TextNode("code block", TEXT_TYPE_CODE),
            TextNode(" and an ", TEXT_TYPE_TEXT),
            TextNode("image", TEXT_TYPE_IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            TextNode(" and a ", TEXT_TYPE_TEXT),
            TextNode("link", TEXT_TYPE_LINK, "https://boot.dev"),
        ]
        self.assertEqual(markdown_to_text_nodes(text), text_nodes)
