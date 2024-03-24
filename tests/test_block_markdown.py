import unittest
from src.block_markdown import markdown_to_blocks


class TestMarkdownToBlocks(unittest.TestCase):
    def test_well_formatted_markdown(self):
        markdown = """
This is **bolded** paragraph

This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
"""
        blocks = [
            "This is **bolded** paragraph",
            "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
            "* This is a list\n* with items",
        ]
        self.assertEqual(markdown_to_blocks(markdown), blocks)

    def test_poorly_formatted_markdown(self):
        markdown = """

# Hello, World



OK, goodbye



"""
        blocks = ["# Hello, World", "OK, goodbye"]
        self.assertEqual(markdown_to_blocks(markdown), blocks)
