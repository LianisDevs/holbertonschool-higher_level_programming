#!/usr/bin/python3
"""This is the pascal_triangle function module"""


def pascal_triangle(n):
    """
    pascal_triangle function
    Parameters: n - this is an int and size of the pascal_triangle
    Returns: list of lists of ints representing Pascal's triangle of n
             if n is <= 0 returns empty list
    """
    if n <= 0:
        return []
    triangle_list = []
    for x in range(n):
        new_list = [1]
        if x > 0:
            for y in range(x - 1):
                prev_list = triangle_list[x - 1]
                val_1 = prev_list[y]
                try:
                    val_2 = prev_list[y + 1]
                except IndexError:
                    val_2 = 0
                result = val_1 + val_2
                new_list.append(result)
            new_list.append(1)
        triangle_list.append(new_list)
    return triangle_list
