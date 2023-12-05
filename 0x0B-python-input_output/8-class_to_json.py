#!/usr/bin/python3
"""
    this module defines a method named class_to_json
"""


def class_to_json(obj):
    """
        returns the dictionary description with simple data structure
    """
    return obj.__dict__
