#!/usr/bin/python3
'''
    This module has a function named print_square(size)
    This function has a test file in tests directory
    size is the size length of the square

'''


def print_square(size):
    '''
        This is a function that prints a square with the character #.
        size is the size length of the square
        size must be an integer, otherwise raise a TypeError
        if size is less than 0, raise a ValueError
        if size is a float and is less than 0, raise a TypeError
    '''
    if type(size) is not int:
        raise TypeError("size must be an integer")
    elif isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    else:
        for i in range(size):
            for j in range(size):
                print("#", end="")
            print()
