#!/usr/bin/python3
"""This is the module containing the square class"""


class Square:
    """
    This is the Square class

    Parameters:
    size: this is the size of the square
    """

    # called when a new square is made
    def __init__(self, size=0):
        self.size = size

    # getter
    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if isinstance(value, int):
            if value < 0:
                raise ValueError("size must be >= 0")
            self.__size = value
        else:
            raise TypeError("size must be an integer")

    def area(self):
        return self.__size ** 2

    def my_print(self):
        for x in range(self.__size):
            for x in range(self.__size):
                print("#", end="")
            print()
