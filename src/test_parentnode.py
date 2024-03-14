import unittest
from node_markdown import *
from node_html import *
from node_text import *


class TestParentNode(unittest.TestCase):
    def test_parent_with_leaves(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "Italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>Italic text</i>Normal text</p>",
        )

    def test_parent_with_parents(self):
        node = ParentNode(
            "p",
            [
                ParentNode(
                    "div", [LeafNode("p", "hello there"), LeafNode("p", "bye for now")]
                ),
                ParentNode(
                    "span", [LeafNode("p", "hello again"), LeafNode("p", "sayonara")]
                ),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><div><p>hello there</p><p>bye for now</p></div><span><p>hello again</p><p>sayonara</p></span></p>",
        )

    def test_deeply_nested_parents(self):
        node = ParentNode(
            "div",
            [
                ParentNode(
                    "div",
                    [
                        ParentNode(
                            "div",
                            [
                                ParentNode(
                                    "div", [LeafNode("p", "Wow!", {"class": "wow"})]
                                )
                            ],
                        )
                    ],
                )
            ],
        )
        self.assertEqual(
            node.to_html(),
            '<div><div><div><div><p class="wow">Wow!</p></div></div></div></div>',
        )


if __name__ == "__main__":
    unittest.main()
