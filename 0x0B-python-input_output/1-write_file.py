#!/usr/bin/python3
'''
This module contains one function:
--------------------------------------
write_file
--------------------------------------
'''


def write_file(filename="", text=""):
    ''' Writes string to text file and returns number of characters written '''

    nb_characters = 0

    with open(filename, 'w') as f:
        for letter in text:
            f.write(letter)
            nb_characters += 1

    return nb_characters
