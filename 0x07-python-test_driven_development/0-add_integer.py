#!/usr/bin/python3
'''
This is the add_integer module.

This module contains one function, add_integer().
'''


def add_integer(a, b=98):
    ''' This function adds 2 integers'''

    if type(a) is float:
        a = int(a)

    if type(b) is float:
        b = int(b)

    if type(a) is not int:
        raise TypeError("a must be an integer")
    elif type(b) is not int:
        raise TypeError("b must be an integer")
    else:
        return a + b
