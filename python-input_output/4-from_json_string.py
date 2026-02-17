#!/usr/bin/python3
"""
This is the module containing from_json_string function
"""
import json


def from_json_string(my_str):
    """
    This is the from_json_string function

    Parameters: my_str
    Returns: object (Python data structure)
    """
    obj = json.loads(my_str)
    return obj
