#!/usr/bin/python3

"""This is the Student module"""


class Student():
    """
    Student Class
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is not None:
            if isinstance(attrs, list):
                if all(isinstance(item, str) for item in attrs):
                    result = self.__dict__
                    return {key: value for key, value
                            in result.items() if key in attrs}
        return self.__dict__
