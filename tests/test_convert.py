import unittest
from src.convert import *


class TestBlockToHTMLParagraph(unittest.TestCase):
    def test_simple_paragraph(self):
        block = "Here is a simple paragraph with some **bold** text in it."
        self.assertEqual(
            block_to_html_paragraph(block).to_html(),
            "<p>Here is a simple paragraph with some <b>bold</b> text in it.</p>",
        )

    def test_complex_paragraph(self):
        block = "**Behold** a more *elusive* and `fascinating` example with a [link](https://www.mallard.dev)"
        self.assertEqual(
            block_to_html_paragraph(block).to_html(),
            '<p><b>Behold</b> a more <i>elusive</i> and <code>fascinating</code> example with a <a href="https://www.mallard.dev">link</a></p>',
        )

    def test_long_paragraph_new_lines(self):
        block = """In the beginning God created the heaven and the earth.
And the earth was without form, and void;
and darkness was upon the face of the deep.
And the Spirit of God moved upon the face of the waters.
And God said, Let there be light: and there was light.
And God saw the light, that it was good:
and God divided the light from the darkness.
And God called the light Day, and the darkness he called Night.
And the evening and the morning were the first day."""
        self.assertEqual(
            block_to_html_paragraph(block).to_html(),
            "<p>In the beginning God created the heaven and the earth.\nAnd the earth was without form, and void;\nand darkness was upon the face of the deep.\nAnd the Spirit of God moved upon the face of the waters.\nAnd God said, Let there be light: and there was light.\nAnd God saw the light, that it was good:\nand God divided the light from the darkness.\nAnd God called the light Day, and the darkness he called Night.\nAnd the evening and the morning were the first day.</p>",
        )


class TestBlockToHTMLHeading(unittest.TestCase):
    def test_heading_one(self):
        block = "# I wanna be an HTML heading when I grow up!"
        self.assertEqual(
            block_to_html_heading(block).to_html(),
            "<h1>I wanna be an HTML heading when I grow up!</h1>",
        )

    def test_heading_six(self):
        block = "###### I'm just a little guy"
        self.assertEqual(
            block_to_html_heading(block).to_html(), "<h6>I'm just a little guy</h6>"
        )


class TestBlockToHTMLCode(unittest.TestCase):
    def test_code_block(self):
        block = "```\nfor i in range(10):\n    print('hello, world')\n```"
        self.assertEqual(
            block_to_html_code(block).to_html(),
            "<pre><code>\nfor i in range(10):\n    print('hello, world')\n</code></pre>",
        )


class TestBlockToHTMLQuote(unittest.TestCase):
    def test_quote_block(self):
        block = "> If we had some *beer*,\n> we could have **beer and pizza**,\n> if we had *pizza*."
        self.assertEqual(
            block_to_html_quote(block).to_html(),
            "<blockquote>If we had some <i>beer</i>,\nwe could have <b>beer and pizza</b>,\nif we had <i>pizza</i>.</blockquote>",
        )


class TestBlockToHTMLUnorderedList(unittest.TestCase):
    def test_unordered_list_asterisks(self):
        block = "* here is an unordered list\n* It's got some stuff\n* Bippity boppity"
        self.assertEqual(
            block_to_html_unordered_list(block).to_html(),
            "<ul><li>here is an unordered list</li><li>It's got some stuff</li><li>Bippity boppity</li></ul>",
        )

    def test_unordered_list_dashes(self):
        block = "- here is an unordered list\n- It's got some stuff\n- Bippity boppity"
        self.assertEqual(
            block_to_html_unordered_list(block).to_html(),
            "<ul><li>here is an unordered list</li><li>It's got some stuff</li><li>Bippity boppity</li></ul>",
        )

    def test_unordered_list_with_inline(self):
        block = "* here is a **bold** item\n* here is an *italic* one\n* here is a [link](https://www.example.com)\n* and here is some `code`"
        self.assertEqual(
            block_to_html_unordered_list(block).to_html(),
            '<ul><li>here is a <b>bold</b> item</li><li>here is an <i>italic</i> one</li><li>here is a <a href="https://www.example.com">link</a></li><li>and here is some <code>code</code></li></ul>',
        )


class TestBlockToHTMLOrderedList(unittest.TestCase):
    def test_ordered_list_short(self):
        block = "1. here is an ordered list\n2. It's got some stuff\n3. Bippity boppity"
        self.assertEqual(
            block_to_html_ordered_list(block).to_html(),
            "<ol><li>here is an ordered list</li><li>It's got some stuff</li><li>Bippity boppity</li></ol>",
        )

    def test_ordered_list_long(self):
        block = "1. this\n2. one\n3. goes\n4. to\n5. eleven\n6. lol\n7. nice\n8. Spinal\n9. Tap\n10. reference\n11. huh?"
        self.assertEqual(
            block_to_html_ordered_list(block).to_html(),
            "<ol><li>this</li><li>one</li><li>goes</li><li>to</li><li>eleven</li><li>lol</li><li>nice</li><li>Spinal</li><li>Tap</li><li>reference</li><li>huh?</li></ol>",
        )

    def test_ordered_list_with_inline(self):
        block = "1. here is a **bold** item\n2. here is an *italic* one\n3. here is a [link](https://www.example.com)\n4. and here is some `code`"
        self.assertEqual(
            block_to_html_ordered_list(block).to_html(),
            '<ol><li>here is a <b>bold</b> item</li><li>here is an <i>italic</i> one</li><li>here is a <a href="https://www.example.com">link</a></li><li>and here is some <code>code</code></li></ol>',
        )


class TestMarkdownToHTMLNode(unittest.TestCase):
    def test_markdown_to_html(self):
        markdown = """
# Front-end Development is the Worst

Look, front-end development is for script kiddies and soydevs who can't handle the real programming. I mean,
it's just a bunch of divs and spans, right? And css??? It's like, "Oh, I want this to be red, but not thaaaaat
red." What a joke.

Real programmers *code*, not silly markup languages. They code on Arch Linux, not Mac OS, and certainly not
Windows. They use **Vim**, not `VS Code`. They use C, not HTML. Come to the [backend](https://www.boot.dev),
where the real programming happens.
"""
        self.assertEqual(
            markdown_to_html(markdown).to_html(),
            '<div><h1>Front-end Development is the Worst</h1><p>Look, front-end development is for script kiddies and soydevs who can\'t handle the real programming. I mean,\nit\'s just a bunch of divs and spans, right? And css??? It\'s like, "Oh, I want this to be red, but not thaaaaat\nred." What a joke.</p><p>Real programmers <i>code</i>, not silly markup languages. They code on Arch Linux, not Mac OS, and certainly not\nWindows. They use <b>Vim</b>, not <code>VS Code</code>. They use C, not HTML. Come to the <a href="https://www.boot.dev">backend</a>,\nwhere the real programming happens.</p></div>',
        )
