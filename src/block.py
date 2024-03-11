import re


def markdown_to_blocks(text):
    block_list = []
    block = ""
    for line in text.splitlines(True):
        if line == "\n":
            block_list.append(block)
            block = ""
        else:
            block += line.strip(" ").strip("\t")
    block_list.append(block)
    while "" in block_list:
        block_list.remove("")
    print(block_list)
    return block_list
