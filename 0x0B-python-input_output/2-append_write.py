#!/usr/bin/python3
"""
    This module defines a methode named append_write
"""


def append_write(filename="", text=""):
    """
        appends a string at the end of a text file UTF8
        returns the number of char added
    """
    with open(filename, 'a', encoding="utf-8") as f:
        f_content = f.write(text)
    return f_content
