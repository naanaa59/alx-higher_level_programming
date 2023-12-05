#!/usr/bin/python3
"""
    This module defines a method named save_to_json_file
"""
import json


def save_to_json_file(my_obj, filename):
    """
        writes an Object to a text file using JSON
    """
    json_rep = json.dumps(my_obj)
    with open(filename, 'w') as f:
        f.write(json_rep)
