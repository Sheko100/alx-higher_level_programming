#!/usr/bin/pyhton3
"""Module for defining the Base class
"""
import json


class Base:
    """class that is the base of all other classes

    Attributes:
        __nb_objects (int): classes count
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """initializes an instance object of Base class

        Args:
            id (int): instance id
        """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """Serializes the list of dictionaries to JSON

        Args:
            list_dictionaries (list): list of dictionaries

        Returns:
            str: JSON respresentation on success or 
            empty list if list_dictionaries is empty or None
        """

        if list_dictionaries is None or len(list_dictionaries) < 1:
            return "[]"

        jsons = json.dumps(list_dictionaries)

        return jsons

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes JSON representaion of list_objs to a file

        Args:
            list_objs (list): a list of objects
        """

        filename = "{}.json".format(cls.__name__)
        dictlist = []

        if list_objs is not None:
            for obj in list_objs:
                dictlist.append(obj.to_dictionary())

        jsons = cls.to_json_string(dictlist)
        with open(filename, mode="w", encoding="utf-8") as file:
            file.write(jsons)
