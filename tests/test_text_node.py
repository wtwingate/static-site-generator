import pytest
from src.text_node import TextNode


class TestTextNodeEqual:
    def test_equal(self):
        textnode1 = TextNode("Sample text", "bold", "https://www.mallard.dev")
        textnode2 = TextNode("Sample text", "bold", "https://www.mallard.dev")
        assert textnode1 == textnode2

    def test_unequal(self):
        textnode1 = TextNode("Sample text", "bold", "https://www.mallard.dev")
        textnode2 = TextNode("Different text", "italic", "https://www.example.com")
        assert textnode1 != textnode2
