from parentnode import ParentNode
from leafnode import LeafNode
import unittest


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


if __name__ == "__main__":
    unittest.main()
