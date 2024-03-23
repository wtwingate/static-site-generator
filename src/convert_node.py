from src.text_node import TextNode
from src.leaf_node import LeafNode
from src.constants import *


def text_node_to_leaf_node(text_node: TextNode) -> LeafNode:
    if text_node.text_type == TEXT_TYPE_TEXT:
        return LeafNode(None, text_node.text)
    elif text_node.text_type == TEXT_TYPE_BOLD:
        return LeafNode("b", text_node.text)
    elif text_node.text_type == TEXT_TYPE_ITALIC:
        return LeafNode("i", text_node.text)
    elif text_node.text_type == TEXT_TYPE_CODE:
        return LeafNode("code", text_node.text)
    elif text_node.text_type == TEXT_TYPE_LINK:
        return LeafNode("a", text_node.text, {"href": text_node.url})
    elif text_node.text_type == TEXT_TYPE_IMAGE:
        return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
    else:
        raise ValueError("Error: invalid text type")


def split_nodes_delimiter(old_nodes: list, delimiter: str, text_type: str) -> list:
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TEXT_TYPE_TEXT:
            new_nodes.append(node)
            continue

        split_strings = node.text.split(delimiter)
        if len(split_strings) % 2 == 0:
            raise Exception("Error: invalid Markdown syntax")

        for index, value in enumerate(split_strings):
            if index % 2 == 0:
                new_nodes.append(TextNode(value, TEXT_TYPE_TEXT))
            else:
                new_nodes.append(TextNode(value, text_type))

    return [node for node in new_nodes if node.text != ""]
