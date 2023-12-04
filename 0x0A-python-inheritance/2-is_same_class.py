#!/usr/bin/python3
"""
    this module define a function same class

"""


def is_same_class(obj, a_class):
    """
        returns True if the object is exactly an instance of given
        class
    """
    return type(obj) is a_class
