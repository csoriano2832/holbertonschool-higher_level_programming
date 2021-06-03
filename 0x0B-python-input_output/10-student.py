#!/usr/bin/python3
'''
This module defines one class
-----------------------------
Student():

and its attributes
-----------------------------
first_name
last_name
age
-----------------------------
'''


class Student():
    ''' Student class definition '''

    def __init__(self, first_name, last_name, age):
        ''' Constructor method '''

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        ''' Retrieves a dictionary representation of a Student instance '''

        class_attributes = self.__dict__
        attributes_retrieved = dict()

        if attrs is not None:

            for index in attrs:
                if index in class_attributes:
                    attributes_retrieved[index] = class_attributes[index]

            return attributes_retrieved

        return class_attributes
