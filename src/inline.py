from textnode import TextNode
import re


def extract_markdown_images(text):
    image_regex = re.compile(r"!\[(.*?)\]\((.*?)\)")
    matches = image_regex.findall(text)
    return matches


def extract_markdown_links(text):
    link_regex = re.compile(r"\[(.*?)\]\((.*?)\)")
    matches = link_regex.findall(text)
    return matches


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != "text":
            new_nodes.append(node)
            continue

        split_text = node.text.split(delimiter)
        if len(split_text) % 2 == 0:
            raise Exception(f"Invalid Markdown syntax: unclosed {delimiter}")

        for index, text in enumerate(split_text):
            if len(text) == 0:
                continue
            if index % 2 == 0:
                new_nodes.append(TextNode(text, "text"))
            else:
                new_nodes.append(TextNode(text, text_type))
    return new_nodes
