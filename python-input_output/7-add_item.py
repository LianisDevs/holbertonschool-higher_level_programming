#!/usr/bin/python3

import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

"""
This is the module containing the add_item function
"""


def add_item(file_name):
    """
    This is the add_item function

    Parameters: file_name
    """
    args = sys.argv
    orig = []
    try:
        orig = load_from_json_file(file_name)
    except FileNotFoundError:
        pass
    finally:
        length = len(args)
        for i in range(1, length):
            orig.append(args[i])

    save_to_json_file(orig, file_name)
