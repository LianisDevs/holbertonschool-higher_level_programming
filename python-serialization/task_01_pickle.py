#!/usr/bin/python3

"""
This is the task_01_pickle module
Contains: CustomObject class
"""

import pickle
from typing import Type


class CustomObject():

    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if isinstance(value, str):
            self.__name = value
        else:
            raise TypeError("Name must be a string")

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if isinstance(value, int):
            self.__age = value
        else:
            raise TypeError("Age must be an int")

    @property
    def is_student(self):
        return self.__is_student

    @is_student.setter
    def is_student(self, value):
        if isinstance(value, bool):
            self.__is_student = value
        else:
            raise TypeError("Is_student must be a bool")

    def display(self):
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Is Student: {}".format(self.is_student))

    def serialize(self, filename):
        with open(filename, "wb") as file:
            pickle.dump(self, file)

    @classmethod
    def deserialize(cls, filename):
        try:
            with open(filename, "rb") as file:
                obj = pickle.load(file)
                return obj
        except FileNotFoundError:
            return None
        except pickle.UnpicklingError:
            return None
        except EOFError:
            return None
