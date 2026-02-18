#!/usr/bin/python3
"""
This is the module containing the load_from_json_file function
"""

import json


def load_from_json_file(filename):
    """
    This is the load_from_json_file function

    Parameters: filename
    """
    with open(filename, "r") as file:
        obj = json.load(file)
        return obj
