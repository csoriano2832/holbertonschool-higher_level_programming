#!/usr/bin/python3
''' This module contains the Square class '''


class Square:
    ''' This class defines the attributes and methods of a square '''

    def __init__(self, size=0, position=(0, 0)):
        ''' Constructor method creates a new instance of a square '''
        self.__size = size
        self.__position = position

    @property
    def size(self):
        ''' Getter method for size attribute '''
        return self.__size

    @size.setter
    def size(self, value):
        ''' Setter method for size attribute '''
        if type(value) is int:
            if value < 0:
                raise ValueError("size must be >= 0")
            self.__size = value
        else:
            raise TypeError("size must be an integer")

    @property
    def position(self):
        ''' Getter method for position attribute '''
        return self.__position

    @position.setter
    def position(self, value):
        ''' Setter method for position attribute '''
        if type(value) is tuple and len(value) == 2:
            if type(value[0]) is int and type(value[1]) is int:
                if value[0] >= 0 and value[1] >= 0:
                    self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        ''' Returns the current square area '''
        return self.__size**2

    def my_print(self):
        ''' Prints in stdout the square with the character # '''
        size = self.__size
        x, y = self.__position

        if size == 0:
            print()
        else:
            for col in range(size):
                while y > 0:
                    print()
                    y -= 1
                for space in range(x):
                    print(" ", end="")
                for row in range(size):
                    print("#", end="")
                print()
