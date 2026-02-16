#!/usr/bin/python3
"""
This is the module containing the read_file function
"""


def read_file(filename=""):
    if  not filename:
        return

    file = open(filename, "r")
    print(file.read())
