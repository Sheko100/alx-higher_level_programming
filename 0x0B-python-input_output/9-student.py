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

    def to_json(self):
        """retrieves a dictionary representation of a Student
        """
        return self.__dict__
