#!/usr/bin/python3
'''
    This module define a method named write_file
'''


def write_file(filename="", text=""):
    """
        writes a string to a text file
    """
    with open(filename, 'w', encoding="utf-8") as myFile:
        file_content = myFile.write(text)
    return file_content
