from textnode import TextNode
from textnode import split_nodes_delimiter
import unittest


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold", "https://www.boot.dev")
        node2 = TextNode("This is a text node", "bold", "https://www.boot.dev")
        self.assertEqual(node, node2)

    def test_none(self):
        node = TextNode("This is a text node", "bold", None)
        node2 = TextNode("This is a text node", "bold", None)
        self.assertEqual(node, node2)

    def test_uneq1(self):
        node = TextNode("This is a text node", "bold", "https://www.boot.dev")
        node2 = TextNode(
            "This is a different text node", "bold", "https://www.boot.dev"
        )
        self.assertNotEqual(node, node2)

    def test_uneq2(self):
        node = TextNode("This is a text node", "italic", "https://www.boot.dev")
        node2 = TextNode("This is a text node", "bold", "https://www.boot.dev")
        self.assertNotEqual(node, node2)

    def test_uneq3(self):
        node = TextNode("This is a text node", "bold", "https://www.boot.dev")
        node2 = TextNode("This is a text node", "bold", "https://www.boots_is_bae.dev")
        self.assertNotEqual(node, node2)


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


if __name__ == "__main__":
    unittest.main()
