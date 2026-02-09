#!/usr/bin/python3
""" This is the 3-is_kind_of_class module."""


def is_kind_of_class(obj, a_class):
    """
    Checks if obj is an instance of a_class or
    instance of a class that inherited from the specific class

    Parameters:
    obj : object to check
    a_class: class to check if obj is an instance of

    Returns:
    True or False

    """
    if isinstance(obj, a_class):
        return True
    return False
