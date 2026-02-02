#!/usr/bin/python3
"""This is the module containing the square class"""


class Square:
    """
    This is the Square class

    Parameters:
    size: this is the size of the square
    """

    __size = 0

    def __init__(self, size=0):
        if isinstance(size, int):
            if size < 0:
                raise ValueError("size must be >= 0")
            self.__size = size
        else:
            raise TypeError("size must be an integer")

    def area(self):
        return self.__size ** 2
