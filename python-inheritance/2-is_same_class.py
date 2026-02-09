#!/usr/bin/python3
""" This is the 2-is_same_class module."""


def is_same_class(obj, a_class):
    """
    Checks if obj is exactly an instance of a_class

    Parameters:
    obj : object to check
    a_class: class to check if obj is an instance of

    Returns:
    True or False

    """
    if type(obj) is a_class:
        return True
    return False
