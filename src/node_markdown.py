import re
from type_text import *
from type_block import *
from node_text import TextNode
from node_text import text_node_to_html
from node_text import block_to_block_type
from node_html import ParentNode


def markdown_to_blocks(text):
    block_list = []
    for line in text.split("\n\n"):
        block_list.append(line.strip())
    while "" in block_list:
        block_list.remove("")
    return block_list


def markdown_to_text_nodes(text):
    raw_text_node = TextNode(text, text_type_text)
    text_nodes = []
    text_nodes.append(raw_text_node)
    text_nodes = split_nodes_delimiter(text_nodes, "**", text_type_bold)
    text_nodes = split_nodes_delimiter(text_nodes, "*", text_type_italic)
    text_nodes = split_nodes_delimiter(text_nodes, "`", text_type_code)
    text_nodes = split_nodes_image(text_nodes)
    text_nodes = split_nodes_link(text_nodes)
    return text_nodes


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
        if node.text_type != text_type_text:
            new_nodes.append(node)
            continue
        split_text = node.text.split(delimiter)
        if len(split_text) % 2 == 0:
            raise Exception(f"Invalid Markdown syntax: unclosed {delimiter}")
        for index, text in enumerate(split_text):
            if len(text) == 0:
                continue
            if index % 2 == 0:
                new_nodes.append(TextNode(text, text_type_text))
            else:
                new_nodes.append(TextNode(text, text_type))
    return new_nodes


def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != text_type_text:
            new_nodes.append(node)
            continue
        matches = extract_markdown_images(node.text)
        if len(matches) == 0:
            new_nodes.append(node)
            continue
        current_text = node.text
        for match in matches:
            split_text = current_text.split(f"![{match[0]}]({match[1]})", 1)
            if len(split_text) != 2:
                raise Exception("Invalid Markdown syntax")
            if split_text[0] != "":
                new_nodes.append(TextNode(split_text[0], text_type_text))
            new_nodes.append(TextNode(match[0], text_type_image, match[1]))
            current_text = split_text[1]
        if current_text != "":
            new_nodes.append(TextNode(current_text, text_type_text))
    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != text_type_text:
            new_nodes.append(node)
            continue
        matches = extract_markdown_links(node.text)
        if len(matches) == 0:
            new_nodes.append(node)
            continue
        current_text = node.text
        for match in matches:
            split_text = current_text.split(f"[{match[0]}]({match[1]})", 1)
            if len(split_text) != 2:
                raise Exception("Invalid Markdown syntax")
            if split_text[0] != "":
                new_nodes.append(TextNode(split_text[0], text_type_text))
            new_nodes.append(TextNode(match[0], text_type_link, match[1]))
            current_text = split_text[1]
        if current_text != "":
            new_nodes.append(TextNode(current_text, text_type_text))
    return new_nodes


def markdown_to_html_node(markdown):
    markdown_blocks = markdown_to_blocks(markdown)
    html_nodes = []
    for block in markdown_blocks:
        if block_to_block_type(block) == block_type_heading:
            html_nodes.append(block_to_html_heading(block))
        elif block_to_block_type(block) == block_type_paragraph:
            html_nodes.append(block_to_html_paragraph(block))
        elif block_to_block_type(block) == block_type_code:
            html_nodes.append(block_to_html_code(block))
        elif block_to_block_type(block) == block_type_quote:
            html_nodes.append(block_to_html_quote(block))
        elif block_to_block_type(block) == block_type_unordered_list:
            html_nodes.append(block_to_html_unordered_list(block))
        elif block_to_block_type(block) == block_type_ordered_list:
            html_nodes.append(block_to_html_ordered_list(block))
    return ParentNode("div", html_nodes)


def block_to_html_heading(block):
    heading = re.match(r"^#+\s", block).group()
    text_nodes = markdown_to_text_nodes(block.replace(heading, ""))
    html_nodes = []
    for node in text_nodes:
        html_nodes.append(text_node_to_html(node))
    return ParentNode(f"h{len(heading) - 1}", html_nodes)


def block_to_html_paragraph(block):
    block = re.sub(r"\n", " ", block)
    text_nodes = markdown_to_text_nodes(block)
    html_nodes = []
    for node in text_nodes:
        html_nodes.append(text_node_to_html(node))
    return ParentNode("p", html_nodes)


def block_to_html_code(block):
    text_nodes = markdown_to_text_nodes(block)
    html_nodes = []
    for node in text_nodes:
        node.text = node.text.strip()
        html_nodes.append(text_node_to_html(node))
    return ParentNode("pre", html_nodes)


def block_to_html_quote(block):
    block = re.sub(r"^>\s", "", block)
    block = re.sub(r"\n>\s", " ", block)
    text_nodes = markdown_to_text_nodes(block)
    html_nodes = []
    for node in text_nodes:
        html_nodes.append(text_node_to_html(node))
    return ParentNode("blockquote", html_nodes)


def block_to_html_unordered_list(block):
    list_items = []
    if block.startswith("*"):
        block = re.sub(r"^\*\s", "", block)
        list_items = re.split(r"\n\*\s", block)
    else:
        block = re.sub(r"^\-\s", "", block)
        list_items = re.split(r"\n\-\s", block)
    while "" in list_items:
        list_items.remove("")
    html_nodes = []
    for item in list_items:
        list_nodes = []
        text_nodes = markdown_to_text_nodes(item)
        for node in text_nodes:
            list_nodes.append(text_node_to_html(node))
        html_nodes.append(ParentNode("li", list_nodes))
    return ParentNode("ul", html_nodes)


def block_to_html_ordered_list(block):
    block = re.sub(r"^1\.\s", "", block)
    list_items = re.split(r"\n\d+\.\s", block)
    while "" in list_items:
        list_items.remove("")
    html_nodes = []
    for item in list_items:
        list_nodes = []
        text_nodes = markdown_to_text_nodes(item)
        for node in text_nodes:
            list_nodes.append(text_node_to_html(node))
        html_nodes.append(ParentNode("li", list_nodes))
    return ParentNode("ol", html_nodes)


def extract_title(markdown):
    lines = markdown.splitlines()
    for line in lines:
        if line.startswith("# "):
            return line.lstrip("# ")
    raise Exception("Page does not contain h1 heading")
