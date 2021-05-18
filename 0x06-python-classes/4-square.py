#!/usr/bin/python3
'''This module contains the Square class'''


class Square:
    '''This class defines the attributes and methods of a square'''

    def __init__(self, size=0):
        '''This method creates a new instance of a square'''
        self.__size = size

    def area(self):
        '''This method calculates the area of a square and returns it'''
        return self.__size**2

    @property
    def size(self):
        '''Getter method for size'''
        return self.__size

    @size.setter
    def size(self, value):
        '''Setter method for size'''
        try:
            self.__size = value
            if value < 0:
                raise ValueError("size must be >= 0")
        except TypeError:
            raise TypeError("size must be an integer")
