#!/usr/bin/python3
import math


class MagicClass():
    """This class contains the methods area and circumference"""

    def __init__(self, radius=0):
        """Constructor method"""
        if type(radius) is not int or if type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Returns the area"""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Returns the circumference"""
        return 2 * math.pi * self.__radius
