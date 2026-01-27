#!/usr/bin/python3

def no_c(my_string):
    chars_to_remove = "cC"

    translation_table = str.maketrans('', '', chars_to_remove)
    new_string = my_string.translate(translation_table)
    return new_string
