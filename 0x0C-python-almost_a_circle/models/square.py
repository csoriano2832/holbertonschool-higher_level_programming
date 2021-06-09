#!/usr/bin/python3
'''
This module defines the following classes:
-----------------------------------------
    Square(Rectangle)

'''
from models.rectangle import Rectangle


class Square(Rectangle):
    '''Defines the methods and attributes of a Square'''
    def __init__(self, size, x=0, y=0, id=None):
        '''Constructor method'''
        super().__init__(size, size, x, y, id)

    def __str__(self):
        '''String representation of a Square'''
        return "[Square] ({:d}) {:d}/{:d} - {:d}"\
            .format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        '''Getter method'''
        return self.width

    @size.setter
    def size(self, value):
        '''Setter method'''
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        '''Assigns a new value to n number of attributes'''
        if len(args) > 0:
            for index in range(len(args[:5])):
                if index == 0:
                    self.id = args[index]
                if index == 1:
                    self.size = args[index]
                if index == 2:
                    self.x = args[index]
                if index == 3:
                    self.y = args[index]
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "size":
                    self.size = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

    def to_dictionary(self):
        '''Returns dictionary representation of a Square'''
        a_dict = {}

        a_dict["size"] = self.width
        a_dict["x"] = self.x
        a_dict["y"] = self.y
        a_dict["id"] = self.id

        return a_dict
