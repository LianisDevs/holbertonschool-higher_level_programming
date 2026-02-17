#!/usr/bin/python3
"""
This is the module containing to_json_string function
"""

import json


def to_json_string(my_obj):
    """
    This is the to_json_string function

    Parameters: my_obj
    Returns: JSON representation of object (string)
    """
    json_string = json.dumps(my_obj)
    return json_string
