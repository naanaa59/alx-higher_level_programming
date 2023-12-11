#!/usr/bin/python3
"""
    This module defines a class named Base
"""
import json
import os
from collections import OrderedDict
import csv


class Base():
    """
        Private class attribute: __nb_objects = 0
        Methods :
            __init__(self, id=None)
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
            class constructor
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
            returns the JSON string representation
        """
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
            writes JSON string representation of list_objs to a file
        """
        with open("{}.json".format(cls.__name__), 'w') as file:
            if list_objs is None:
                empty_list = []
                file.write(cls.to_json_string(empty_list))
            else:
                json_list = [obj.to_dictionary() for obj in list_objs]
                json_string = cls.to_json_string(json_list)
                file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """
            returns the list of the JSON string representation
        """
        if json_string is None or len(json_string) == 0:
            empty_list = []
            return empty_list
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
            returns an instance with all attributes already set
        """
        if cls.__name__ == "Rectangle":
            obj_r = cls(1, 1)
            obj_r.update(**dictionary)
            return obj_r

        if cls.__name__ == "Square":
            obj_s = cls(1)
            obj_s.update(**dictionary)
            return obj_s

    @classmethod
    def load_from_file(cls):
        """
            returns a list of instances
        """
        filename = "{}.json".format(cls.__name__)
        if os.path.exists(filename):
            with open(filename, 'r') as file:
                return [cls.create(**d) for d in cls.from_json_string(file.read())]
        else:
            empty_list = []
            return empty_list

    @classmethod
    def save_to_file_csv(cls, list_objs):
        '''Saves object to csv file.'''
        from models.rectangle import Rectangle
        from models.square import Square
        if list_objs is not None:
            if cls is Rectangle:
                list_objs = [[o.id, o.width, o.height, o.x, o.y]
                             for o in list_objs]
            else:
                list_objs = [[o.id, o.size, o.x, o.y]
                             for o in list_objs]
        with open('{}.csv'.format(cls.__name__), 'w', newline='',
                  encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerows(list_objs)

    @classmethod
    def load_from_file_csv(cls):
        '''Loads object to csv file.'''
        from models.rectangle import Rectangle
        from models.square import Square
        ret = []
        with open('{}.csv'.format(cls.__name__), 'r', newline='',
                  encoding='utf-8') as f:
            reader = csv.reader(f)
            for row in reader:
                row = [int(r) for r in row]
                if cls is Rectangle:
                    d = {"id": row[0], "width": row[1], "height": row[2],
                         "x": row[3], "y": row[4]}
                else:
                    d = {"id": row[0], "size": row[1],
                         "x": row[2], "y": row[3]}
                ret.append(cls.create(**d))
        return ret

    @staticmethod
    def draw(list_rectangles, list_squares):
        import turtle
        import time
        from random import randrange
        turtle.Screen().colormode(255)
        for i in list_rectangles + list_squares:
            t = turtle.Turtle()
            t.color((randrange(255), randrange(255), randrange(255)))
            t.pensize(1)
            t.penup()
            t.pendown()
            t.setpos((i.x + t.pos()[0], i.y - t.pos()[1]))
            t.pensize(10)
            t.forward(i.width)
            t.left(90)
            t.forward(i.height)
            t.left(90)
            t.forward(i.width)
            t.left(90)
            t.forward(i.height)
            t.left(90)
            t.end_fill()

        time.sleep(5)
