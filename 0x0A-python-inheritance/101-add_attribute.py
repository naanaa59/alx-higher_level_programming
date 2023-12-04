#!/usr/bin/python3
"""
    This module defines a method to add a new attribute
"""


def add_attribute(objec, attribute, value):
    """
        add a new attribute if possible
    """
    if hasattr(objec, "__dict__"):
        setattr(objec, attribute, value)
    else:
        raise TypeError("can't add new attribute")
