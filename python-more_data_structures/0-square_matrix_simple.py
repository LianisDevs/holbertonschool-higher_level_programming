#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    square_it = lambda num: num * num
    squared_matrix = [list(map(square_it, row)) for row in matrix]

    return squared_matrix
