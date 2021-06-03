#!/usr/bin/python3
import json
'''
This module contains one function:
----------------------------------
from_json_string()
----------------------------------
'''


def from_json_string(my_str):
    ''' Returns an object represented by a JSON string '''

    return json.loads(my_str)
