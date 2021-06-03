#!/usr/bin/python3
import json
import sys
'''
This module contains two functions:
-------------------------------------
save_to_json_file(my_obj, filename)
load_from_json_file(filename)
-------------------------------------
'''


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

jfile = "add_item.json"
a_list = []

try:
    a_list = load_from_json_file(jfile)
except:
    pass

for index in range(1, len(sys.argv)):
    a_list.append(sys.argv[index])

save_to_json_file(a_list, jfile)
