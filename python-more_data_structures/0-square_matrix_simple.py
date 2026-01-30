#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    squared_matrix = [list(map(square_it, row)) for row in matrix]
    return squared_matrix


def square_it(num):
    return num * num
