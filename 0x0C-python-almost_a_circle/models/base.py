#!/usr/bin/python3
'''
This module defines the following classes:
----------------------------------------------
    Base()

'''
import json


class Base():
    '''This class will be the base of all other classes'''
    __nb_objects = 0

    def __init__(self, id=None):
        '''Constructor method'''

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation"""

        if not list_dictionaries or len(list_dictionaries) == 0:
            return "[]"

        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation to a file"""

        a_list = []

        if list_objs:
            for index in list_objs:
                a_list.append(index.to_dictionary())

        json_str = cls.to_json_string(a_list)

        with open("{:s}.json".format(cls.__name__), 'w') as f:
            f.write(json_str)

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation"""

        if not json_string or len(json_string) == 0:
            return "[]"

        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set"""
        from models.rectangle import Rectangle
        from models.square import Square

        if cls == Rectangle:
            dummy_instance = cls(3, 5)

        if cls == Square:
            dummy_instance = cls(4)

        dummy_instance.update(**dictionary)

        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances from a file with JSON object"""

        inst_list = []

        try:
            open("{:s}.json".format(cls.__name__))
        except:
            return []

        with open("{:s}.json".format(cls.__name__)) as f:
            inst_obj = cls.from_json_string(f.read())
            for inst_dict in inst_obj:
                inst_list.append(cls.create(**inst_dict))
            return inst_list
