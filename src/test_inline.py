import unittest
from text_node import *


class TestSplitNodesDelimiter(unittest.TestCase):
    def test_bold(self):
        old_nodes = [
            TextNode("Here is some **bold** text", text_type_text),
            TextNode("**SUCH BOLDNESS**", text_type_text),
            TextNode("Not very bold at all", text_type_text),
        ]
        self.assertEqual(
            split_nodes_delimiter(old_nodes, "**", text_type_bold),
            [
                TextNode("Here is some ", text_type_text),
                TextNode("bold", text_type_bold),
                TextNode(" text", text_type_text),
                TextNode("SUCH BOLDNESS", text_type_bold),
                TextNode("Not very bold at all", text_type_text),
            ],
        )

    def test_italic(self):
        old_nodes = [
            TextNode("Here is some *italic* text", text_type_text),
            TextNode("*Mama Mia! That's a spicy meat-a-ball!*", text_type_text),
            TextNode("Nothing to see here", text_type_text),
        ]
        self.assertEqual(
            split_nodes_delimiter(old_nodes, "*", text_type_italic),
            [
                TextNode("Here is some ", text_type_text),
                TextNode("italic", text_type_italic),
                TextNode(" text", text_type_text),
                TextNode("Mama Mia! That's a spicy meat-a-ball!", text_type_italic),
                TextNode("Nothing to see here", text_type_text),
            ],
        )

    def test_code(self):
        old_nodes = [
            TextNode("Here is some `code` text", text_type_text),
            TextNode("`print('hello, world')`", text_type_text),
            TextNode("I'm a luddite!", text_type_text),
        ]
        self.assertEqual(
            split_nodes_delimiter(old_nodes, "`", text_type_code),
            [
                TextNode("Here is some ", text_type_text),
                TextNode("code", text_type_code),
                TextNode(" text", text_type_text),
                TextNode("print('hello, world')", text_type_code),
                TextNode("I'm a luddite!", text_type_text),
            ],
        )

    def test_bad_syntax(self):
        old_nodes = [
            TextNode("Here is some invalid **bold text", text_type_text),
        ]
        with self.assertRaises(Exception):
            split_nodes_delimiter(old_nodes, "**", text_type_bold)


class TestSplitNodesImage(unittest.TestCase):
    def test_one_image(self):
        old_nodes = [
            TextNode(
                "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) holy Moses!",
                text_type_text,
            )
        ]
        self.assertEqual(
            split_nodes_image(old_nodes),
            [
                TextNode("This is text with an ", text_type_text),
                TextNode("image", text_type_image, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" holy Moses!", text_type_text),
            ],
        )

    def test_two_images(self):
        old_nodes = [
            TextNode(
                "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
                text_type_text,
            )
        ]
        self.assertEqual(
            split_nodes_image(old_nodes),
            [
                TextNode("This is text with an ", text_type_text),
                TextNode("image", text_type_image, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", text_type_text),
                TextNode(
                    "second image", text_type_image, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
        )

    def test_all_images(self):
        old_nodes = [
            TextNode(
                "![duck](https://www.mallard.dev/duck.png)![duck](https://www.mallard.dev/duck.png)![goose](https://www.mallard.dev/goose.png)",
                text_type_text,
            )
        ]
        self.assertEqual(
            split_nodes_image(old_nodes),
            [
                TextNode("duck", text_type_image, "https://www.mallard.dev/duck.png"),
                TextNode("duck", text_type_image, "https://www.mallard.dev/duck.png"),
                TextNode("goose", text_type_image, "https://www.mallard.dev/goose.png"),
            ],
        )

    def test_no_images(self):
        old_nodes = [
            TextNode(
                "This is just a plain old boring text with no images at all",
                text_type_text,
            ),
            TextNode(
                "What did the waiter say when he brought out the eggs benedict on a hubcap?",
                text_type_text,
            ),
            TextNode(
                "There's no place like chrome for the hollandaise!", text_type_text
            ),
        ]
        self.assertEqual(
            split_nodes_image(old_nodes),
            [
                TextNode(
                    "This is just a plain old boring text with no images at all",
                    text_type_text,
                ),
                TextNode(
                    "What did the waiter say when he brought out the eggs benedict on a hubcap?",
                    text_type_text,
                ),
                TextNode(
                    "There's no place like chrome for the hollandaise!", text_type_text
                ),
            ],
        )


class TestSplitNodesLink(unittest.TestCase):
    def test_one_link(self):
        old_nodes = [
            TextNode(
                "This is text with an [link](https://www.example.com)",
                text_type_text,
            )
        ]
        self.assertEqual(
            split_nodes_link(old_nodes),
            [
                TextNode("This is text with an ", text_type_text),
                TextNode("link", text_type_link, "https://www.example.com"),
            ],
        )

    def test_two_links(self):
        old_nodes = [
            TextNode(
                "This is text with an [link](https://www.example.com) and another [second link](https://www.example.com)",
                text_type_text,
            )
        ]
        self.assertEqual(
            split_nodes_link(old_nodes),
            [
                TextNode("This is text with an ", text_type_text),
                TextNode("link", text_type_link, "https://www.example.com"),
                TextNode(" and another ", text_type_text),
                TextNode("second link", text_type_link, "https://www.example.com"),
            ],
        )

    def test_all_links(self):
        old_nodes = [
            TextNode(
                "[duck](https://www.mallard.dev/duck)[duck](https://www.mallard.dev/duck)[goose](https://www.mallard.dev/goose)",
                text_type_text,
            )
        ]
        self.assertEqual(
            split_nodes_link(old_nodes),
            [
                TextNode("duck", text_type_link, "https://www.mallard.dev/duck"),
                TextNode("duck", text_type_link, "https://www.mallard.dev/duck"),
                TextNode("goose", text_type_link, "https://www.mallard.dev/goose"),
            ],
        )

    def test_no_images(self):
        old_nodes = [
            TextNode(
                "This is just a plain old boring text with no images at all",
                text_type_text,
            ),
            TextNode(
                "What did the waiter say when he brought out the eggs benedict on a hubcap?",
                text_type_text,
            ),
            TextNode(
                "There's no place like chrome for the hollandaise!", text_type_text
            ),
        ]
        self.assertEqual(
            split_nodes_link(old_nodes),
            [
                TextNode(
                    "This is just a plain old boring text with no images at all",
                    text_type_text,
                ),
                TextNode(
                    "What did the waiter say when he brought out the eggs benedict on a hubcap?",
                    text_type_text,
                ),
                TextNode(
                    "There's no place like chrome for the hollandaise!", text_type_text
                ),
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


class TestTextToTextNodes(unittest.TestCase):
    def test_markdown_to_text1(self):
        text = "This is **text** with an *italic* word and a `code block` and an ![image](https://i.imgur.com/zjjcJKZ.png) and a [link](https://boot.dev)"
        self.assertEqual(
            text_to_textnodes(text),
            [
                TextNode("This is ", text_type_text),
                TextNode("text", text_type_bold),
                TextNode(" with an ", text_type_text),
                TextNode("italic", text_type_italic),
                TextNode(" word and a ", text_type_text),
                TextNode("code block", text_type_code),
                TextNode(" and an ", text_type_text),
                TextNode("image", text_type_image, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and a ", text_type_text),
                TextNode("link", text_type_link, "https://boot.dev"),
            ],
        )

    def test_markdown_to_text2(self):
        text = "**This line is** *only made up* **of weird markdown** `syntax`"
        self.assertEqual(
            text_to_textnodes(text),
            [
                TextNode("This line is", text_type_bold),
                TextNode(" ", text_type_text),
                TextNode("only made up", text_type_italic),
                TextNode(" ", text_type_text),
                TextNode("of weird markdown", text_type_bold),
                TextNode(" ", text_type_text),
                TextNode("syntax", text_type_code),
            ],
        )
