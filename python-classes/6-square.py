#!/usr/bin/python3
"""This is the module containing the square class"""


class Square:
    """
    This is the Square class

    Parameters:
    size: this is the size of the square
    """

    # called when a new square is made
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

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
        return self.size ** 2

    def my_print(self):
        if self.size > 0:
            for x in range(self.size):
                for y in range(self.size):
                    print("#", end="")
                print()
        else:
            print()

    # getter
    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if isinstance(value, tuple):
            if len(value) != 2:
                raise TypeError
                ("position must be a tuple of 2 positive integers")

            if all(isinstance(x, int) for x in value):
                self.__position = value
            else:
                raise TypeError
                ("position must be a tuple of 2 positive integers")
 
        else:
            raise TypeError("position must be a tuple of 2 positive integers")
