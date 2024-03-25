import os
import shutil
from src.convert import markdown_to_html


def main():
    reset_public_dir()
    copy_directory_tree("static", "public")
    generate_pages_recursive("./content", "./template.html", "./public")


def copy_directory_tree(from_path, dest_path):
    dir_list = os.listdir(from_path)
    for item in dir_list:
        item_path = os.path.join(from_path, item)
        copy_path = os.path.join(dest_path, item)
        if os.path.isfile(item_path):
            print(f"Copying {item_path} to {copy_path}...")
            shutil.copy(item_path, copy_path)
        else:
            os.mkdir(copy_path)
            copy_directory_tree(item_path, copy_path)


def reset_public_dir():
    if os.path.exists("./public"):
        shutil.rmtree("./public")
    os.mkdir("./public")


def generate_pages_recursive(from_path, template_path, dest_path):
    dir_list = os.listdir(from_path)
    for item in dir_list:
        item_path = os.path.join(from_path, item)
        publish_path = os.path.join(dest_path, item)
        if os.path.isfile(item_path):
            if publish_path.endswith(".md"):
                publish_path = publish_path.replace(".md", ".html")
            generate_page(item_path, template_path, publish_path)
        else:
            generate_pages_recursive(item_path, template_path, publish_path)


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path) as f:
        markdown = f.read()
    with open(template_path) as f:
        template = f.read()
    html_content = markdown_to_html(markdown).to_html()
    html_title = extract_title(markdown)
    template = template.replace("{{ Title }}", html_title)
    template = template.replace("{{ Content }}", html_content)
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    with open(dest_path, "w") as f:
        f.write(template)


def extract_title(markdown):
    lines = markdown.splitlines()
    for line in lines:
        if line.startswith("# "):
            return line.lstrip("# ")
    raise Exception("Page does not contain h1 heading")


main()
