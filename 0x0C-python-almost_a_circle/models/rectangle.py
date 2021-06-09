#!/usr/bin/python3
'''
This module defines the following classes:
------------------------------------------
    Rectangle(Base)

'''
from models.base import Base


class Rectangle(Base):
    '''Defines attributes and methods of the class Rectangle'''

    @property
    def width(self):
        '''Getter method'''
        return self.__width

    @width.setter
    def width(self, value):
        '''Setter method'''
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        '''Getter method'''
        return self.__height

    @height.setter
    def height(self, value):
        '''Setter method'''
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        '''Getter method'''
        return self.__x

    @x.setter
    def x(self, value):
        '''Setter method'''
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        '''Getter method'''
        return self.__y

    @y.setter
    def y(self, value):
        '''Setter method'''
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def __init__(self, width, height, x=0, y=0, id=None):
        '''Constructor method'''
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def area(self):
        '''Returns the area of a Rectangle instance'''
        return self.width * self.height

    def display(self):
        '''Prints in stdout the Rectangle instance with the character #'''
        for vertical_shift in range(self.y):
            print()
        for column in range(self.height):
            for horizontal_shift in range(self.x):
                print(" ", end="")
            for row in range(self.width):
                print("#", end="")
            print()

    def __str__(self):
        '''Overrides the __str__ method'''
        return "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}"\
            .format(self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        '''Assigns an argument to each attribute'''
        if len(args) > 0:
            for index in range(len(args[:5])):
                if index == 0:
                    self.id = args[index]
                if index == 1:
                    self.width = args[index]
                if index == 2:
                    self.height = args[index]
                if index == 3:
                    self.x = args[index]
                if index == 4:
                    self.y = args[index]
        else:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value
                if key == 'width':
                    self.width = value
                if key == 'height':
                    self.height = value
                if key == 'x':
                    self.x = value
                if key == 'y':
                    self.y = value

    def to_dictionary(self):
        '''Returns dictionary representation of a Rectangle'''
        a_dict = {}

        a_dict["width"] = self.width
        a_dict["height"] = self.height
        a_dict["x"] = self.x
        a_dict["y"] = self.y
        a_dict["id"] = self.id

        return a_dict
