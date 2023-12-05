#!/usr/bin/python3
"""
    This is a module defines a class named Student
"""


class Student():
    """
        Public instance attributes:
            first_name
            last_name
            age
        Method:
            to_json
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__
        else:
            for attr in attrs:
                attr_dic = {tuple(attrs): self.__dict__.get(attr)}
            return attr_dic
