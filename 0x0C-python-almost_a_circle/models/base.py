#!/usr/bin/pyhton3
"""Module for defining the Base class
"""
import json
import os
import csv
import turtle


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

    @staticmethod
    def from_json_string(json_string):
        """Deserializes JSON string to a list of dictionaries

        Args:
            json_string (str): a JSON string

        Returns:
            list: a list of dictionaries if the string is legit or
            empty list if the string is None or empty list
        """

        dctlist = []
        if json_string is not None:
            dctlist = json.loads(json_string)

        return dctlist

    @classmethod
    def create(cls, **dictionary):
        """Creates an instance with all attributes already set"""

        clsname = cls.__name__

        if clsname == "Rectangle":
            obj = cls(2, 1)
        elif clsname == "Square":
            obj = cls(2)
        obj.update(**dictionary)

        return obj

    @classmethod
    def load_from_file(cls):
        """Reads a list of dictionaries in JSON representation from a file

        Returns:
            list: list of instances
        """
        objlist = []
        filename = "{}.json".format(cls.__name__)

        if os.path.isfile(filename):
            with open(filename, encoding="utf-8") as file:
                jsons = file.read()

            dctlist = cls.from_json_string(jsons)
            for objdct in dctlist:
                newobj = cls.create(**objdct)
                objlist.append(newobj)

            return objlist

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Writes list of objects to a file in CSV format

        Args:
            list_objs (list): list of objects
        """

        clsname = cls.__name__
        filename = "{}.csv".format(clsname)
        rows = []
        rectkeys = ["id", "width", "height", "x", "y"]
        sqkeys = ["id", "size", "x", "y"]

        if list_objs is not None:
            for obj in list_objs:
                row = []
                objdct = obj.to_dictionary()
                if clsname == "Rectangle":
                    keys = rectkeys
                elif clsname == "Square":
                    keys = sqkeys
                for key in keys:
                    row.append(objdct[key])
                rows.append(row)

        with open(filename, mode="w", encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile)
            for row in rows:
                writer.writerow(row)

    @classmethod
    def load_from_file_csv(cls):
        """Reads CSV file into list of objects"""

        clsname = cls.__name__
        filename = "{}.csv".format(clsname)
        rows = []
        objlist = []
        rectkeys = ["id", "width", "height", "x", "y"]
        sqkeys = ["id", "size", "x", "y"]

        if os.path.isfile(filename):
            with open(filename, encoding="utf-8") as csvfile:
                csvdata = csv.reader(csvfile)
                rows = list(csvdata)
            for row in rows:
                i = 0
                objdct = {}
                if clsname == "Rectangle":
                    keys = rectkeys
                elif clsname == "Square":
                    keys = sqkeys
                for key in keys:
                    objdct[key] = int(row[i])
                    i += 1
                newobj = cls.create(**objdct)
                objlist.append(newobj)

        return (objlist)

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draws rectangles and squares on a new window"""
        colors = ["red", "yellow", "blue", "green", "brown"]
        window = turtle.Screen()
        i = 0
        for rect in list_rectangles:
            if i == 5:
                i = 0
            rectpen = turtle.RawPen(window)
            rectpen.up()
            rectpen.color("black", colors[i])
            rectpen.begin_fill()
            rectpen.speed(1)
            rectpen.hideturtle()
            rectpen.setpos(rect.x, rect.y)
            rectpen.down()
            rectpen.forward(rect.width)
            rectpen.setheading(270)
            rectpen.forward(rect.height)
            rectpen.setheading(180)
            rectpen.forward(rect.width)
            rectpen.setheading(90)
            rectpen.forward(rect.height)
            rectpen.end_fill()
            i += 1

        for sq in list_squares:
            if i == 5:
                i = 0
            sqpen = turtle.RawPen(window)
            sqpen.up()
            sqpen.color("black", colors[i])
            sqpen.begin_fill()
            sqpen.speed(1)
            sqpen.hideturtle()
            sqpen.setpos(sq.x, sq.y)
            sqpen.down()
            sqpen.forward(sq.size)
            sqpen.setheading(270)
            sqpen.forward(sq.size)
            sqpen.setheading(180)
            sqpen.forward(sq.size)
            sqpen.setheading(90)
            sqpen.forward(sq.size)
            sqpen.end_fill()
            i += 1

        turtle.exitonclick()
