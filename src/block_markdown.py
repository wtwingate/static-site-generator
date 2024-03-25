import re
from constants import *


def markdown_to_blocks(markdown: str) -> list:
    blocks = []
    split_lines = markdown.split("\n\n")
    for line in split_lines:
        blocks.append(line.strip())
    while "" in blocks:
        blocks.remove("")
    return blocks


def block_to_block_type(block):
    lines = block.split("\n")
    if re.match(r"^#{1,6}\s\w+", block):
        return BLOCK_TYPE_HEADING
    if block.startswith("```") and block.endswith("```"):
        return BLOCK_TYPE_CODE
    if all(line.startswith(">") for line in lines):
        return BLOCK_TYPE_QUOTE
    if all(line.startswith("*") for line in lines):
        return BLOCK_TYPE_UNORDERED_LIST
    if all(line.startswith("-") for line in lines):
        return BLOCK_TYPE_UNORDERED_LIST
    if block.startswith("1."):
        for index, line in enumerate(lines):
            if not line.startswith(f"{index + 1}. "):
                return BLOCK_TYPE_PARAGRAPH
        return BLOCK_TYPE_ORDERED_LIST
    return BLOCK_TYPE_PARAGRAPH
