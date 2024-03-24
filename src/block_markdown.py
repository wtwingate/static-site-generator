def markdown_to_blocks(markdown: str) -> list:
    blocks = []
    split_lines = markdown.split("\n\n")
    for line in split_lines:
        blocks.append(line.strip())
    while "" in blocks:
        blocks.remove("")
    return blocks
