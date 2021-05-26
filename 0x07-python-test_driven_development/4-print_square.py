#!/usr/bin/python3
'''This module defines one method'''


def print_square(size):
    '''This method prints a square'''

    if type(size) is not int or (type(size) is float and size < 0):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for col in range(size):
        for row in range(size):
            print("#", end="")
        print()
