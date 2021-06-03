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

    def to_json(self):
        ''' Retrieves a dictionary representation of a Student instance '''

        return self.__dict__
