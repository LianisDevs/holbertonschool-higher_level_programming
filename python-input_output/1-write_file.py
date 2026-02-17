#!/usr/bin/python3
"""
This is the module containing the write_file function
"""


def write_file(file_name="", text=""):
    """
    This is the write_file function

    Parameters: file_name and text
    Returns: number of chars written
    """
    with open(file_name, "w") as file:
        num_chars_written = file.write(text)

    return num_chars_written
