import os
import re
import shutil


def main():
    reset_public_dir()
    copy_directory_tree("static")


def copy_directory_tree(dir_path):
    dir_list = os.listdir(dir_path)
    for item in dir_list:
        item_path = os.path.join(dir_path, item)
        copy_path = re.sub(r"^static", "public", item_path)
        if os.path.isfile(item_path):
            shutil.copy(item_path, copy_path)
        else:
            os.mkdir(copy_path)
            copy_directory_tree(item_path)


def reset_public_dir():
    if os.path.exists("./public"):
        shutil.rmtree("./public")
    os.mkdir("./public")


main()
