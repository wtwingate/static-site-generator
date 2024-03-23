import re


def extract_markdown_links(text: str) -> list:
    link_regex = re.compile(r"\[(.*?)\]\((.*?)\)")
    return re.findall(link_regex, text)


def extract_markdown_images(text: str) -> list:
    image_regex = re.compile(r"!\[(.*?)\]\((.*?)\)")
    return re.findall(image_regex, text)
