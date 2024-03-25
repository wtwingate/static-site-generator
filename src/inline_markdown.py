import re
from text_node import TextNode
from constants import *


def markdown_to_text_nodes(markdown: str) -> list:
    nodes = [TextNode(markdown, TEXT_TYPE_TEXT)]
    nodes = split_nodes_delimiter(nodes, "**", TEXT_TYPE_BOLD)
    nodes = split_nodes_delimiter(nodes, "*", TEXT_TYPE_ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TEXT_TYPE_CODE)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes


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


def extract_markdown_links(text: str) -> list:
    link_regex = re.compile(r"\[(.*?)\]\((.*?)\)")
    return re.findall(link_regex, text)


def extract_markdown_images(text: str) -> list:
    image_regex = re.compile(r"!\[(.*?)\]\((.*?)\)")
    return re.findall(image_regex, text)


def split_nodes_link(old_nodes: list) -> list:
    new_nodes = []
    for node in old_nodes:
        markdown_links = extract_markdown_links(node.text)
        if len(markdown_links) == 0:
            new_nodes.append(node)
            continue
        original_text = node.text
        for link_tuple in markdown_links:
            split_text = original_text.split(f"[{link_tuple[0]}]({link_tuple[1]})", 1)
            new_nodes.append(TextNode(split_text[0], TEXT_TYPE_TEXT))
            new_nodes.append(TextNode(link_tuple[0], TEXT_TYPE_LINK, link_tuple[1]))
            original_text = split_text[1]
        new_nodes.append(TextNode(original_text, TEXT_TYPE_TEXT))
    return [node for node in new_nodes if node.text != ""]


def split_nodes_image(old_nodes: list) -> list:
    new_nodes = []
    for node in old_nodes:
        markdown_images = extract_markdown_images(node.text)
        if len(markdown_images) == 0:
            new_nodes.append(node)
            continue
        original_text = node.text
        for image_tuple in markdown_images:
            split_text = original_text.split(
                f"![{image_tuple[0]}]({image_tuple[1]})", 1
            )
            new_nodes.append(TextNode(split_text[0], TEXT_TYPE_TEXT))
            new_nodes.append(TextNode(image_tuple[0], TEXT_TYPE_IMAGE, image_tuple[1]))
            original_text = split_text[1]
        new_nodes.append(TextNode(original_text, TEXT_TYPE_TEXT))
    return [node for node in new_nodes if node.text != ""]
