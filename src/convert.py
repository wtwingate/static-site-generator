import re
from parent_node import ParentNode
from leaf_node import text_node_to_leaf_node
from block_markdown import *
from inline_markdown import *
from constants import *


def markdown_to_html(markdown):
    html_nodes = []
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        html_nodes.append(block_to_html(block))
    return ParentNode("div", html_nodes)


def block_to_html(block):
    block_type = block_to_block_type(block)
    if block_type == BLOCK_TYPE_HEADING:
        return block_to_html_heading(block)
    if block_type == BLOCK_TYPE_PARAGRAPH:
        return block_to_html_paragraph(block)
    if block_type == BLOCK_TYPE_QUOTE:
        return block_to_html_quote(block)
    if block_type == BLOCK_TYPE_CODE:
        return block_to_html_code(block)
    if block_type == BLOCK_TYPE_ORDERED_LIST:
        return block_to_html_ordered_list(block)
    if block_type == BLOCK_TYPE_UNORDERED_LIST:
        return block_to_html_unordered_list(block)


def markdown_to_leaf_nodes(markdown):
    text_nodes = markdown_to_text_nodes(markdown)
    leaf_nodes = []
    for text_node in text_nodes:
        leaf_node = text_node_to_leaf_node(text_node)
        leaf_nodes.append(leaf_node)
    return leaf_nodes


def block_to_html_heading(block):
    heading_level = 0
    for char in block:
        if char == "#":
            heading_level += 1
        else:
            break
    children = markdown_to_leaf_nodes(block[heading_level + 1 :])
    return ParentNode(f"h{heading_level}", children)


def block_to_html_paragraph(block):
    children = markdown_to_leaf_nodes(block)
    return ParentNode("p", children)


def block_to_html_quote(block):
    lines = block.split("\n")
    text = "\n".join([line[2:] for line in lines])
    children = markdown_to_leaf_nodes(text)
    return ParentNode("blockquote", children)


def block_to_html_code(block):
    children = markdown_to_leaf_nodes(block[4:-3])
    code = [ParentNode("code", children)]
    return ParentNode("pre", code)


def block_to_html_ordered_list(block):
    lines = block.split("\n")
    children = []
    for line in lines:
        line = re.sub(r"\d+\.\s+", "", line)
        leaf_nodes = markdown_to_leaf_nodes(line)
        children.append(ParentNode("li", leaf_nodes))
    return ParentNode("ol", children)


def block_to_html_unordered_list(block):
    lines = block.split("\n")
    children = []
    for line in lines:
        leaf_nodes = markdown_to_leaf_nodes(line[2:])
        children.append(ParentNode("li", leaf_nodes))
    return ParentNode("ul", children)
