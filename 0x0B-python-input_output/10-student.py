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
        if type(attrs) is list and all(type(att) is str for att in attrs):
            return {attr: getattr(self, attr) for
                    attr in attrs if hasattr(self, attr)}
        return self.__dict__
