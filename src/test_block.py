import unittest
from block import *


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
                "# This is a heading",
                "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
                "* This is a list item\n* This is another list item",
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
                "This is a **bolded** paragraph\nAnd here is an *italicized* line in the same paragraph.",
                "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
                "* This is a list\n* with items\n* so many items",
            ],
        )

    def test_multiple_newlines(self):
        markdown = """


This should be the first block






And this should be the second


        """
        self.assertEqual(
            markdown_to_blocks(markdown),
            ["This should be the first block", "And this should be the second"],
        )


class TestBlockToBlockType(unittest.TestCase):
    def test_heading_one_valid(self):
        block = "# Heading 1"
        self.assertEqual(block_to_block_type(block), block_type_heading)

    def test_heading_one_valid(self):
        block = "###### Heading 6"
        self.assertEqual(block_to_block_type(block), block_type_heading)

    def test_heading_too_long(self):
        block = "####### Heading 7"
        self.assertEqual(block_to_block_type(block), block_type_paragraph)

    def test_heading_missing_space(self):
        block = "##Heading 2"
        self.assertEqual(block_to_block_type(block), block_type_paragraph)

    def test_code_valid(self):
        block = "```print('hello, world')```"
        self.assertEqual(block_to_block_type(block), block_type_code)

    def test_code_valid_multiline(self):
        block = "```for i in range(10):\n    print('hello, world')```"
        print(block)
        self.assertEqual(block_to_block_type(block), block_type_code)

    def test_code_invalid(self):
        block = "```print('hello, world')"
        self.assertEqual(block_to_block_type(block), block_type_paragraph)

    def test_code_invalid(self):
        block = "``print('hello, world')````"
        self.assertEqual(block_to_block_type(block), block_type_paragraph)

    def test_quote_valid(self):
        block = "> Here is a block quote\n> It is three lines long\n>Wowzers"
        self.assertEqual(block_to_block_type(block), block_type_quote)

    def test_quote_invalid(self):
        block = "> Here is a block quote\nOops! forgot to put a > here\n>Wowzers"
        self.assertEqual(block_to_block_type(block), block_type_paragraph)

    def test_unordered_list_asterisks(self):
        block = "* this is an unordered list\n* another item\n* final item"
        self.assertEqual(block_to_block_type(block), block_type_unordered_list)

    def test_unordered_list_dashes(self):
        block = "- this is an unordered list\n- another item\n- final item"
        self.assertEqual(block_to_block_type(block), block_type_unordered_list)

    def test_unordered_list_missing(self):
        block = "* this is an unordered list\nOopsie daisy!\n* final item"
        self.assertEqual(block_to_block_type(block), block_type_paragraph)

    def test_unordered_list_mixed(self):
        block = "* this is an unordered list\n- That's mix up\n* final item"
        self.assertEqual(block_to_block_type(block), block_type_paragraph)

    def test_ordered_list_valid(self):
        block = "1. Ordered list incoming\n2. Second item\n3. Fourth item\n4. Wait a second..."
        self.assertEqual(block_to_block_type(block), block_type_ordered_list)

    def test_ordered_list_missing(self):
        block = "1. Ordered list incoming\n2. Second item\nA wild missingno. appeared\n4. Fourth item"
        self.assertEqual(block_to_block_type(block), block_type_paragraph)

    def test_ordered_list_out_of_order(self):
        block = "1. Ordered list incoming\n3. Second item\n4. Fourth item\n2. Wait a second..."
        self.assertEqual(block_to_block_type(block), block_type_paragraph)


if __name__ == "__main__":
    unittest.main()
