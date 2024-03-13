import re
from block_type import *


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
    if re.match(r"^(`{3}).*(`{3})$", block):
        return block_type_code
    if all(line[0] == ">" for line in lines):
        return block_type_quote
    if all(line[0] == "*" for line in lines):
        return block_type_unordered_list
    if all(line[0] == "-" for line in lines):
        return block_type_unordered_list
    if (
        block.startswith("1.")
        and all(re.match(r"^\d+\.", line) for line in lines)
        # check if the list is numbered sequentially
        and all(
            int(lines[i][0]) == int(lines[i + 1][0]) - 1 for i in range(len(lines) - 1)
        )
    ):
        return block_type_ordered_list
    return block_type_paragraph
