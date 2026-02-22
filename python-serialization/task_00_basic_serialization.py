#!/usr/bin/python3
"""
This is the serialize module
Containing the serialize_and_save_to_file function
and load_and_deserialize function
"""

import pickle


def serialize_and_save_to_file(data, filename):
    """
    serialize_and_save_to_file function
    Parameters: data to serialize and filename to save the data to
    """
    with open(filename, 'wb') as file:
        pickle.dump(data, file)


def load_and_deserialize(filename):
    """
    load_and_deserialize function
    Parameters: filename to load data from
    Return: original data
    """
    with open(filename, 'rb') as file:
        original_data = pickle.load(file)
        return original_data
