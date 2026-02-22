#!/usr/bin/python3
"""
This is the task_00_basic_serialization module
Containing the serialize_and_save_to_file function
and load_and_deserialize function
"""

import json


def serialize_and_save_to_file(data, filename):
    """
    serialize_and_save_to_file function
    Parameters: data to serialize and filename to save the data to
    """
    try:
        with open(filename, "w", encoding="utf-8") as file:
            file.write(json.dumps(data))
    except FileNotFoundError:
        raise FileNotFoundError("filename: {} not found".format(filename))


def load_and_deserialize(filename):
    """
    load_and_deserialize function
    Parameters: filename to load data from
    Return: original data
    """
    with open(filename, "r") as file:
        obj = json.load(file)
        return obj
