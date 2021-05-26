#!/usr/bin/python3
'''
This module defines (1) method(s),
----------------------------------------------------

[def matrix_divided(matrix, div)]

----------------------------------------------------
'''


def matrix_divided(matrix, div):
    '''Divides all elements of a matrix'''

    err_message = "matrix must be a matrix (list of lists) of integers/floats"
    if type(matrix) is not list:
        raise TypeError(err_message)

    for outer_row in matrix:
        for inner_row in outer_row:
            if type(inner_row) not in [int, float]:
                raise TypeError(err_message)

    check_row_size = matrix[0]
    for row in matrix:
        if len(check_row_size) != len(row):
            raise TypeError("Each row of the matrix must have the same size")

    if type(div) not in [int, float]:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return list(map(lambda x: list(map(lambda y:
                round(y / div, 2), x)), matrix))
