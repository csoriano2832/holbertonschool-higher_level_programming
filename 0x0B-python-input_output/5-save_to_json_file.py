#!/usr/bin/python3
import json
'''
This module contains one function:
----------------------------------
save_to_json_file()
----------------------------------
'''


def save_to_json_file(my_obj, filename):
    ''' Writes an Object to a text file, using a JSON representation '''

    with open(filename, 'w') as f:
        f.write(json.dumps(my_obj))
