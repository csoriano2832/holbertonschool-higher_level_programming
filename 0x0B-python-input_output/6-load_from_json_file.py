#!/usr/bin/python3
'''
This module contains one function:
----------------------------------
load_from_json_file()
----------------------------------
'''
import json


def load_from_json_file(filename):
    ''' Creates an Object from JSON file '''

    with open(filename) as f:
        for line in f:
            return json.loads(line)
