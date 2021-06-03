#!/usr/bin/python3
''' This class contains one class and its definitions '''


class BaseGeometry():
    ''' Defines the attributes and methods of the class '''

    def area(self):
        ''' Raises an exception '''

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        ''' Validates values '''

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
