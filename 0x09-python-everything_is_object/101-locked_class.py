#!/usr/bin/python3
'''This module contains a LockedClass class'''


class LockedClass:
    '''This class defines a class with only one attribute'''
    __slots__ = ['first_name']

    def __init__(self, value=""):
        '''Constructor method'''
        self.first_name = value
