#!/usr/bin/python3
"""
This is the module containing the read_file function
"""


def read_file(filename=""):
    """
    This is the read_file function

    Parameters: filename
    """
    if  not filename:
        return

    with open(filename, "r") as file:
        print(file.read())
