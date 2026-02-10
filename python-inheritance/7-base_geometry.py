#!/usr/bin/python3
"""This is the module containing the BaseGeometry class"""


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
