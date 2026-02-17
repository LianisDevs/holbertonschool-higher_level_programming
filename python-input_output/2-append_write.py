#!/usr/bin/python3
"""
This is the module containing the append_write function
"""


def append_write(filename="", text=""):
    """
    This is the append_write function

    Parameters: file_name and text
    Returns: number of chars written
    """
    with open(filename, "a") as file:
        num_chars_written = file.write(text)
        return num_chars_written
