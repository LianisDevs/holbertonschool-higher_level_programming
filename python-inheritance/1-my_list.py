#!/usr/bin/python3
""" This is the module containing the MyList class."""


class MyList(list):
    """
    This is the MyList class

    Parameters:
    inherits list: python built-in
    """
    def print_sorted(self):
        print(sorted(self))
