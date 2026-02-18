#!/usr/bin/python3
"""
This is the module containing save_to_json_string function
"""

import json


def save_to_json_file(my_obj, filename):
    """
    This is the save_to_json_string function

    Parameters: my_obj, filename
    """
    with open(filename, "w", encoding="utf-8") as file:
        file.write(json.dumps(my_obj))
