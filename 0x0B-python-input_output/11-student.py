#!/usr/bin/python3
"""Module for Student class
"""


class Student:
    """class defines a student

    Attributes:
        first_name: student first name
        last_name: student last name
        age: student age
    """

    def __init__(self, first_name, last_name, age):
        """initializes a new student

        Args:
            first_name: student first name
            last_name: student last name
            age: student age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student

        Args:
            attr: attributes to include in the dictionary
        """
        dct = {}
        if type(attrs) == list:
            if len(attrs) > 0 and type(attrs[0]) == str:
                for attr in attrs:
                    if attr in self. __dict__:
                        dct[attr] = self.__dict__[attr]
            return dct
        return self.__dict__

    def reload_from_json(self, json):
        """replaces all attributes of the Student instance

        Args:
            json: attributes dictionary in JSON string
        """
        if len(json) > 0:
            self.__dict__ = json
