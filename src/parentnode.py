from htmlnode import HTMLNode


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("Error: parent node must have HTML tag")
        if self.children is None:
            raise ValueError("Error: parent node must have children")
        child_html_list = []
        for child in self.children:
            child_html_list.append(child.to_html())
        child_html_string = "".join(child_html_list)
        return f"<{self.tag}>{child_html_string}</{self.tag}>"

    def __repr__(self):
        return f"ParentNode({self.tag}, {self.children}, {self.props})"
