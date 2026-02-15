"""
This is the FlyingFish module that defines
the Fish, Bird and FlyingFish classes
"""


class Fish():
    """
    This is the Fish class
    """
    def swim(self):
        print("The fish is swimming")

    def habitat(self):
        print("The fish lives in water")


class Bird():
    """
    This is the Bird class
    """
    def fly(self):
        print("The bird is flying")

    def habitat(self):
        print("The bird lives in the sky")


class FlyingFish(Bird, Fish):
    """
    This is the FlyingFish class

    Inherits: Bird and Fish
    """
    def fly(self):
        print("The flying fish is soaring!")

    def swim(self):
        print("The flying fish is swimming!")

    def habitat(self):
        print("The flying fish lives both in water and the sky!")
