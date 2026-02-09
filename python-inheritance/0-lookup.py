#!/usr/bin/python3
"""
This is the 0-lookup module.
"""


def lookup(obj):
    """
    Accesses available attributes and methods of an object

    Parameters:
    obj : object to access attributes and methods of

    Returns:
    list: available attributes and methods of object

    """
    dir_list = dir(obj)
    return dir_list
