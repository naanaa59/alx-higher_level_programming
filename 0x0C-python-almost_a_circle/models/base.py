#!/usr/bin/python3
"""
    This module defines a class named Base
"""


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
