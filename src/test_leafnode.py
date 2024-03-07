import unittest

from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_to_html1(self):
        node = LeafNode("p", "Ducks fly together!")
        self.assertEqual(
            node.to_html(),
            "<p>Ducks fly together!</p>"
        )


    def test_to_html2(self):
        node = LeafNode(None, "Ducks fly together!")
        self.assertEqual(
            node.to_html(),
            "Ducks fly together!"
        )


    def test_to_html3(self):
        node = LeafNode("a", "Click here for more ducks!", {"href": "https://www.mallard.dev"})
        self.assertEqual(
            node.to_html(),
            '<a href="https://www.mallard.dev">Click here for more ducks!</a>'
        )


if __name__ == "__main__":
    unittest.main()