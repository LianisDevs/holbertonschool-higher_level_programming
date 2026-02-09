#!/usr/bin/python3
""" This is the 4-inherits_from module."""


def inherits_from(obj, a_class):
    """
    Checks if obj is an instance of a_class that
    inherited directly or indirectly from the specified class

    Parameters:
    obj : object to check
    a_class: class to check

    Returns:
    True or False

    """
    if type(obj) is a_class:
        return False
    if issubclass(type(obj), a_class):
        return True
    return False
