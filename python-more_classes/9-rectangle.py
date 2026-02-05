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
    print_symbol = '#'

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
        string = ""
        for x in range(self.__height):
            string += self.print_symbol.__str__() * self.__width
            if x < self.__height - 1:
                string += "\n"
        return string

    def __repr__(self):
        return ("Rectangle({}, {})".format(self.__width, self.__height))

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        area_1 = Rectangle.area(rect_1)
        area_2 = Rectangle.area(rect_2)
        if area_2 > area_1:
            return rect_2
        else:
            return rect_1

    @classmethod
    def square(cls, size=0):
        # returns a new Rectangle instance
        return cls(size, size)
