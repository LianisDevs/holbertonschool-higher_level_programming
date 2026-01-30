#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    tuple_1 = tuple_processor(tuple_a)
    tuple_2 = tuple_processor(tuple_b)

    sum_0 = tuple_1[0] + tuple_2[0]
    sum_1 = tuple_1[1] + tuple_2[1]
    sum_tuple = (sum_0, sum_1)

    return sum_tuple


def tuple_processor(tuple):
    length = len(tuple)
    if length == 2 or length > 2:
        tuple_temp = (tuple[0], tuple[1])
    elif length == 1:
        tuple_temp = (tuple[0], 0)
    elif length == 0:
        tuple_temp = (0, 0)
    return tuple_temp
