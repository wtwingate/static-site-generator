import unittest
from block import markdown_to_blocks


class TestMarkdownToBlocks(unittest.TestCase):
    def test_multiline_markdown(self):
        markdown = """
        # This is a heading

        This is a paragraph of text. It has some **bold** and *italic* words inside of it.

        * This is a list item
        * This is another list item
        """
        self.assertEqual(
            markdown_to_blocks(markdown),
            [
                "# This is a heading\n",
                "This is a paragraph of text. It has some **bold** and *italic* words inside of it.\n",
                "* This is a list item\n* This is another list item\n",
            ],
        )

    def test_blocks_with_newlines(self):
        markdown = """
        This is a **bolded** paragraph
        And here is an *italicized* line in the same paragraph.

        This is another paragraph with *italic* text and `code` here
        This is the same paragraph on a new line

        * This is a list
        * with items
        * so many items
        """
        self.assertEqual(
            markdown_to_blocks(markdown),
            [
                "This is a **bolded** paragraph\nAnd here is an *italicized* line in the same paragraph.\n",
                "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line\n",
                "* This is a list\n* with items\n* so many items\n",
            ],
        )

    def test_multiple_newlines(self):
        markdown = """


        This should be the first block






        And this should be the second


        """
        self.assertEqual(
            markdown_to_blocks(markdown),
            ["This should be the first block\n", "And this should be the second\n"],
        )
