import re
from type_text import *
from type_block import *
from node_html import LeafNode


class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        return (
            self.text == other.text
            and self.text_type == other.text_type
            and self.url == other.url
        )

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"


def text_node_to_html(text_node):
    if text_node.text_type == text_type_text:
        return LeafNode(None, text_node.text)
    if text_node.text_type == text_type_bold:
        return LeafNode("b", text_node.text)
    if text_node.text_type == text_type_italic:
        return LeafNode("i", text_node.text)
    if text_node.text_type == text_type_code:
        return LeafNode("code", text_node.text)
    if text_node.text_type == text_type_image:
        return LeafNode("img", text_node.text, {"src": text_node.url})
    if text_node.text_type == text_type_link:
        return LeafNode("a", text_node.text, {"href": text_node.url})
    raise Exception(f"Invalid text type: {text_node.text_type}")


def block_to_block_type(block):
    lines = block.split("\n")
    if re.match(r"^#{1,6}\s", block):
        return block_type_heading
    if block.startswith("```") and block.endswith("```"):
        return block_type_code
    if all(line.startswith(">") for line in lines):
        return block_type_quote
    if all(line.startswith("*") for line in lines):
        return block_type_unordered_list
    if all(line.startswith("-") for line in lines):
        return block_type_unordered_list
    if (
        block.startswith("1.")
        and all(re.match(r"^\d+\.\s", line) for line in lines)
        # check if the list is numbered sequentially
        and all(
            int(lines[i][0]) == int(lines[i + 1][0]) - 1 for i in range(len(lines) - 1)
        )
    ):
        return block_type_ordered_list
    return block_type_paragraph
