#!/usr/bin/python3
"""This is the module containing the BaseGeometry and Rectangle class"""


class BaseGeometry:
    """
    This is the BaseGeometry class
    """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if isinstance(value, int) and not isinstance(value, bool):
            if value <= 0:
                raise ValueError("{} must be greater than 0".format(name))
        else:
            raise TypeError("{} must be an integer".format(name))


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
