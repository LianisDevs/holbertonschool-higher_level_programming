#!/usr/bin/python3
"""
This is the module containing the Shape, Circle and Rectangle class

Functions:
shape_info: duck typing concept
"""
from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    """
    This is the abstract Shape class

    Parameters: inherits ABC
    """

    @abstractmethod
    def area(self):
        # each child class must implement this abstractmethod
        pass

    @abstractmethod
    def perimeter(self):
        # each child class must implement this abstractmethod
        pass


class Circle(Shape):
    """
    This is the Circle class

    Parameters: inherits Shape
    """

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * pi * self.radius


class Rectangle(Shape):
    """
    This is the Rectangle class

    Parameters: inherits Shape
    """

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


def shape_info(obj):
    try:
        print("Area: {}".format(obj.area()))
        print("Perimeter: {}".format(obj.perimeter()))
    except Exception:
        print("Shape info error")
