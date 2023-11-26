#!/usr/bin/python3
''' This module has a function named add_integer
    a and b must be integers or floats, otherwise raise a TypeError exception
    with the message a must be an integer or b must be an integer
    a and b must be first casted to integers if they are float
    Returns an integer: the addition of a and b
'''


def add_integer(a, b=98):
    ''' Return the sum int of two numbers a and b
    Args: a might be an integer or float
          b might be an int or float
    Return: an int sum of a and b casted to int if float

    '''
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif isinstance(a, float):
        a = int(a)
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    elif isinstance(b, float):
        b = int(b)
    return a + b
