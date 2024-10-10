import sys
import pathlib
from colorama import Fore, Back, Style

processing_dir = pathlib.Path(sys.argv[1])
directory_content = []


def collect_files(directory):
    if not directory.exists():
        raise FileExistsError("This directory doesn`t exist!")

    for item in directory.iterdir():
        directory_content.append(item)
        if item.is_dir():
            collect_files(item)


def printing_directory(content):
    for item in content:
        item_string = str(item)
        arr = item_string.split('\\')
        indent = '  ' * (len(arr) - 1)

        if item != None and item.is_dir():
            print(Fore.LIGHTBLUE_EX + indent + arr[-1] + '\\')
        else:
            print(Fore.LIGHTGREEN_EX + indent + arr[-1])


collect_files(processing_dir)
printing_directory(directory_content)
