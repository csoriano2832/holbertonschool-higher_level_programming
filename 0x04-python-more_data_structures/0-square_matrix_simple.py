#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix is not None:
        squares = []
        for x in range(len(matrix)):
                squares.append(list(map(lambda x: x**2, matrix[x])))

        return squares
