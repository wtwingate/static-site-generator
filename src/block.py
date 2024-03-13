import re
from block_type import *
from textnode import *


def markdown_to_blocks(text):
    block_list = []
    for line in text.split("\n\n"):
        block_list.append(line.strip())
    while "" in block_list:
        block_list.remove("")
    return block_list


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


def block_to_html_paragraph(block):
    # convert raw markdown to text nodes
    text_nodes = text_to_textnodes(block)
    html_nodes = []
    # convert text nodes to HTML nodes
    for node in text_nodes:
        html_nodes.append(text_node_to_html(node))
    # create html parent node for block with inline children
    return ParentNode("p", html_nodes)
