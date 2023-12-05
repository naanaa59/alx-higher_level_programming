#!/usr/bin/python3
import json
"""
    This module defines a method named to_json_string
"""


def to_json_string(my_obj):
    json_string = json.dumps(my_obj)
    return json_string
