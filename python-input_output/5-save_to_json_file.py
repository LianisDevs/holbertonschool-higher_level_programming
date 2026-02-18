#!/usr/bin/python3
"""
This is the module containing save_to_json_string function
"""

import json


def save_to_json_file(my_obj, filename):
    """
    This is the save_to_json_string function

    Parameters: my_obj, filename
    Returns: JSON representation of object (string)
    """
    json_string = json.dumps(my_obj)
    with open(filename, "w") as file:
        file.write(json_string)
    return json_string
