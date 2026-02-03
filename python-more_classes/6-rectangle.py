#!/usr/bin/python3
"""This is the module containing the rectangle class"""


class Rectangle:
    """
    This is the Rectangle class

    Parameters:
    width: this is the width of the rectangle
    height: this is the height of the rectangle
    area: this is the area of the rectangle (width * height)
    perimeter: this is the perimeter of the rectangle (width + height)
    """

    number_of_instances = 0

    # called when a new rectangle is made
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (self.__width * 2) + (self.__height * 2)

    # for print()
    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        return '\n'.join("#" * self.__width for x in range(self.__height))

    def __repr__(self):
        return ("Rectangle({}, {})".format(self.__width, self.__height))

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
