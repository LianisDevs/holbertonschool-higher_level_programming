#!/usr/bin/python3
"""This is the module containing Rectangle class"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    This is the Rectangle class

    Parameters:
    BaseGeometry: inherits BaseGeometry class

    """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.__width = width

        self.integer_validator("height", height)
        self.__height = height
