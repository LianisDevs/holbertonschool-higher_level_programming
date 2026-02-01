#!/usr/bin/python3
"""
This is the 0-add_integer module.
"""


def add_integer(a, b=98):
    """
    Adds to numbers together.

    Parameters:
    a (int or float) : Value 1 to add
    b (int or float) : Value 2 to add

    Returns:
    int: sum of a and b
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    if a == float('inf'):
        raise OverflowError("float is overflowing")
    try:
        return int(a) + int(b)
    except ValueError:
        raise ValueError("cannot convert float NaN to integer")
