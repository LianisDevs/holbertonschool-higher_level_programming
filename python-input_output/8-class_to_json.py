#!/usr/bin/python3

"""This module contains the class_to_json function"""


def class_to_json(obj):
    """
    class_to_json function
    Parameters: python obj
    Returns: dictionary description for obj
    """
    return obj.__dict__
