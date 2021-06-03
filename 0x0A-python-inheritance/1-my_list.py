#!/usr/bin/python3
''' This module contains the class MyList and it's definitions '''


class MyList(list):
    ''' The class MyList inherits from list and has one method '''

    def print_sorted(self):
        ''' Prints a list, sorted '''

        sorted_list = sorted(self)
        print(sorted_list)
