#!/usr/bin/python3
'''
    This module has a function named say_my_name
    prints My name is <first name> <last name>
'''


def say_my_name(first_name, last_name=""):
    '''
    prints My name is <first name> <last name>

    Args:(string): first_name
         (optional string): last_name
    '''
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    elif not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    elif not first_name:
        print("My name is")
    else:
        print("My name is {} {}".format(first_name, last_name))
