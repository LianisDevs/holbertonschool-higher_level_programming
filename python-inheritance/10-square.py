#!/usr/bin/python3
"""This is the module containing Square class"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    This is the Square class

    Parameters:
    Rectangle: inherits Rectangle class

    """
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size

    def __str__(self):
        return f"[{Rectangle.__name__}] {self.__size}/{self.__size}"

    def area(self):
        area = self.__size ** 2
        return area
