import re


def markdown_to_blocks(text):
    block_list = []
    for line in text.split("\n\n"):
        block_list.append(line.strip())
    while "" in block_list:
        block_list.remove("")
    return block_list
