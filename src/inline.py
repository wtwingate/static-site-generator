import re


def extract_markdown_images(text):
    image_regex = re.compile(r"!\[(.*?)\]\((.*?)\)")
    matches = image_regex.findall(text)
    return matches


def extract_markdown_links(text):
    link_regex = re.compile(r"\[(.*?)\]\((.*?)\)")
    matches = link_regex.findall(text)
    return matches
