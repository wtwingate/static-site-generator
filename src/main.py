import os
import shutil


def main():
    reset_public_dir()
    copy_directory_tree("static", "public")


def copy_directory_tree(dir_path, dest_path):
    dir_list = os.listdir(dir_path)
    print(dir_list)
    for item in dir_list:
        item_path = os.path.join(dir_path, item)
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


main()
