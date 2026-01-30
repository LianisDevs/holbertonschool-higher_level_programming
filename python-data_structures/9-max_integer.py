#!/usr/bin/python3

def max_integer(my_list=[]):
    if not my_list:
        return None

    my_list.sort()
    max_val = my_list[-1]
    return max_val
