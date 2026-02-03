#!/usr/bin/python3
"""This is the module containing the rectangle class"""


class Rectangle:
    """
    This is the Rectangle class

    Parameters:
    width: this is the width of the rectangle
    height: this is the height of the rectangle
    """

    # called when a new rectangle is made
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    # getter
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif not value >= 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    # getter
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif not value >= 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
