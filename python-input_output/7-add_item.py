#!/usr/bin/python3
"""
This is the module containing the add_item function
"""

import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def add_item():
    """
    This is the add_item function
    Loads file, reads file, appends to file and then saves file
    """

    args = sys.argv
    orig = []
    try:
        orig = load_from_json_file("add_item.json")
    except FileNotFoundError:
        pass
    finally:
        length = len(args)
        for i in range(1, length):
            orig.append(args[i])

    save_to_json_file(orig, "add_item.json")


if __name__ == "__main__":
    add_item()
