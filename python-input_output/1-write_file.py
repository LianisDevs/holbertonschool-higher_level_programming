#!/usr/bin/python3
"""
This is the module containing the write_file function
"""


def write_file(file_name="", text=""):
    with open(file_name, "w") as file:
        file.write(text)
