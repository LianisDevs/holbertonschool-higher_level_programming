#!/usr/bin/python3
"""This is the module containing the Animal, Cat and Dog class"""
from abc import ABC, abstractmethod


class Animal(ABC):
    """
    This is the Animal class

    Parameters: inherits ABC
    """
    @abstractmethod
    def sound(self):
        # each child class must implement this function
        pass


class Cat(Animal):
    """
    This is the Cat class

    Parameters: inherits Animal class
    """
    def sound(self):
        return "Meow"


class Dog(Animal):
    """
    This is the Dog class

    Parameters: inherits Animal class
    """
    def sound(self):
        return "Bark"
