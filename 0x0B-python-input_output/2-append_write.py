#!/usr/bin/python3
'''
This module contains one function:
----------------------------------
append_write()
----------------------------------
'''


def append_write(filename="", text=""):
    ''' Appends a string at the end of a text file
    and returns the number of characters added '''

    nb_characters = 0

    with open(filename, 'a') as f:
        for letter in text:
            f.write(letter)
            nb_characters += 1

    return nb_characters
