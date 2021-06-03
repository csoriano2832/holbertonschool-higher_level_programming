#!/usr/bin/python3
''' This module contains two classes and their definitions '''


class BaseGeometry():
    ''' Defines attributes and methods for the class BaseGeometry '''

    def area(self):
        ''' Raises an exception '''

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        ''' Validates values '''

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    ''' Defines attributes and methods for the class Rectangle '''

    def __init__(self, width, height):
        ''' Constructor method '''

        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        ''' Returns the area of a rectangle '''

        return self.__width * self.__height

    def __str__(self):
        ''' String representation of a rectangle '''

        return ("[Rectangle] {}/{}".format(self.__width, self.__height))


class Square(Rectangle):
    ''' Defines attributes and methods for the class Square '''

    def __init__(self, size):
        ''' Constructor method '''

        super().__init__(size, size)
