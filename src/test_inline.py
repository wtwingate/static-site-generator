from inline import split_nodes_delimiter
from inline import split_nodes_image
from inline import split_nodes_link
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


class TestSplitNodesImage(unittest.TestCase):
    def test_one_image(self):
        old_nodes = [
            TextNode(
                "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) holy Moses!",
                "text",
            )
        ]
        self.assertEqual(
            split_nodes_image(old_nodes),
            [
                TextNode("This is text with an ", "text"),
                TextNode("image", "image", "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" holy Moses!", "text"),
            ],
        )

    def test_two_images(self):
        old_nodes = [
            TextNode(
                "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
                "text",
            )
        ]
        self.assertEqual(
            split_nodes_image(old_nodes),
            [
                TextNode("This is text with an ", "text"),
                TextNode("image", "image", "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", "text"),
                TextNode("second image", "image", "https://i.imgur.com/3elNhQu.png"),
            ],
        )

    def test_all_images(self):
        old_nodes = [
            TextNode(
                "![duck](https://www.mallard.dev/duck.png)![duck](https://www.mallard.dev/duck.png)![goose](https://www.mallard.dev/goose.png)",
                "text",
            )
        ]
        self.assertEqual(
            split_nodes_image(old_nodes),
            [
                TextNode("duck", "image", "https://www.mallard.dev/duck.png"),
                TextNode("duck", "image", "https://www.mallard.dev/duck.png"),
                TextNode("goose", "image", "https://www.mallard.dev/goose.png"),
            ],
        )

    def test_no_images(self):
        old_nodes = [
            TextNode(
                "This is just a plain old boring text with no images at all", "text"
            ),
            TextNode(
                "What did the waiter say when he brought out the eggs benedict on a hubcap?",
                "text",
            ),
            TextNode("There's no place like chrome for the hollandaise!", "text"),
        ]
        self.assertEqual(
            split_nodes_image(old_nodes),
            [
                TextNode(
                    "This is just a plain old boring text with no images at all", "text"
                ),
                TextNode(
                    "What did the waiter say when he brought out the eggs benedict on a hubcap?",
                    "text",
                ),
                TextNode("There's no place like chrome for the hollandaise!", "text"),
            ],
        )


class TestSplitNodesLink(unittest.TestCase):
    def test_one_link(self):
        old_nodes = [
            TextNode(
                "This is text with an [link](https://www.example.com)",
                "text",
            )
        ]
        self.assertEqual(
            split_nodes_link(old_nodes),
            [
                TextNode("This is text with an ", "text"),
                TextNode("link", "link", "https://www.example.com"),
            ],
        )

    def test_two_links(self):
        old_nodes = [
            TextNode(
                "This is text with an [link](https://www.example.com) and another [second link](https://www.example.com)",
                "text",
            )
        ]
        self.assertEqual(
            split_nodes_link(old_nodes),
            [
                TextNode("This is text with an ", "text"),
                TextNode("link", "link", "https://www.example.com"),
                TextNode(" and another ", "text"),
                TextNode("second link", "link", "https://www.example.com"),
            ],
        )

    def test_all_links(self):
        old_nodes = [
            TextNode(
                "[duck](https://www.mallard.dev/duck)[duck](https://www.mallard.dev/duck)[goose](https://www.mallard.dev/goose)",
                "text",
            )
        ]
        self.assertEqual(
            split_nodes_link(old_nodes),
            [
                TextNode("duck", "link", "https://www.mallard.dev/duck"),
                TextNode("duck", "link", "https://www.mallard.dev/duck"),
                TextNode("goose", "link", "https://www.mallard.dev/goose"),
            ],
        )

    def test_no_images(self):
        old_nodes = [
            TextNode(
                "This is just a plain old boring text with no images at all", "text"
            ),
            TextNode(
                "What did the waiter say when he brought out the eggs benedict on a hubcap?",
                "text",
            ),
            TextNode("There's no place like chrome for the hollandaise!", "text"),
        ]
        self.assertEqual(
            split_nodes_link(old_nodes),
            [
                TextNode(
                    "This is just a plain old boring text with no images at all", "text"
                ),
                TextNode(
                    "What did the waiter say when he brought out the eggs benedict on a hubcap?",
                    "text",
                ),
                TextNode("There's no place like chrome for the hollandaise!", "text"),
            ],
        )


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
