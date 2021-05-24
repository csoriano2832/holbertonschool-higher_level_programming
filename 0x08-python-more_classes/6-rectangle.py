#!/usr/bin/python3
"""This module contains the class Rectangle"""


class Rectangle:
    """Defines a rectangle"""
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Instantiation"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """retrieve width"""
        return self.__width

    @width.setter
    def width(self, value):
        """set width"""
        if type(value) is int:
            if value >= 0:
                self.__width = value
            else:
                raise ValueError("width must be >= 0")
        else:
            raise TypeError("width must be an integer")

    @property
    def height(self):
        """retrieve height"""
        return self.__height

    @height.setter
    def height(self, value):
        """set height"""
        if type(value) is int:
            if value >= 0:
                self.__height = value
            else:
                raise ValueError("height must be >= 0")
        else:
            raise TypeError("height must be an integer")

    def area(self):
        """Returns area of a rectangle"""
        return self.width * self.height

    def perimeter(self):
        """Returns perimeter of a rectangle"""
        if self.width == 0 or self.height == 0:
            return 0
        return 2 *(self.width + self.height)

    def __str__(self):
        """Prints the rectangle using the # character """
        str_rectangle = ""

        for col in range(self.height):
            for row in range(self.width):
                str_rectangle += "#"
            if col != (self.height - 1):
                str_rectangle += "\n"

        return str_rectangle

    def __repr__(self):
        """String representation of the rectangle to be able to recreate a new
        instance by using eval()"""

        return ("Rectangle({}, {})".format(self.width, self.height))

    def __del__(self):
        """Prints message when instance of Rectangle is deleted"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
