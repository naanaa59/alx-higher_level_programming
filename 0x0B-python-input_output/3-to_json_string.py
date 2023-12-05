#!/usr/bin/python3
"""
    This module defines a method named to_json_string
"""

import json


def to_json_string(my_obj):
    """
        eturns the JSON representation of an object (string)
    """
    json_string = json.dumps(my_obj)
    return json_string
