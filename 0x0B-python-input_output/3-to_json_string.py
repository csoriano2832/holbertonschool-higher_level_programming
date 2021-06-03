#!/usr/bin/python3
import json
'''
This module contains one function:
----------------------------------
to_json_string()
----------------------------------
'''


def to_json_string(my_obj):
    ''' Returns the JSON representation of an object '''

    return json.dumps(my_obj)
