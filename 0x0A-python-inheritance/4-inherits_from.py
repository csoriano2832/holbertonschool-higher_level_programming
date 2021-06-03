#!/usr/bin/python3
''' This module contains one function '''


def inherits_from(obj, a_class):
    '''
    Returns true if object is an instance of a class that inherited from the
    specified class ; otherwise False
    '''

    if type(obj) != a_class:
        return issubclass(obj.__class__, a_class)
    else:
        return False
