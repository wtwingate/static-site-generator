from html_node import HTMLNode
from text_node import TextNode
from constants import *


class LeafNode(HTMLNode):
    def __init__(
        self,
        tag: str | None,
        value: str,
        props: dict | None = None,
    ) -> None:
        super().__init__(tag, value, None, props)

    def to_html(self) -> str:
        if self.value is None:
            raise ValueError("Error: leaf nodes must have a value")
        if self.tag is None:
            return f"{self.value}"
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"


def text_node_to_leaf_node(text_node: TextNode) -> LeafNode:
    if text_node.text_type == TEXT_TYPE_TEXT:
        return LeafNode(None, text_node.text)
    elif text_node.text_type == TEXT_TYPE_BOLD:
        return LeafNode("b", text_node.text)
    elif text_node.text_type == TEXT_TYPE_ITALIC:
        return LeafNode("i", text_node.text)
    elif text_node.text_type == TEXT_TYPE_CODE:
        return LeafNode("code", text_node.text)
    elif text_node.text_type == TEXT_TYPE_LINK:
        return LeafNode("a", text_node.text, {"href": text_node.url})
    elif text_node.text_type == TEXT_TYPE_IMAGE:
        return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
    else:
        raise ValueError("Error: invalid text type")
