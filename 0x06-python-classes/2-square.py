#!/usr/bin/python3
"""
Module name: square_module

This module defines a class named Square

Class:
    Square: defines a square

Attributes:
    Size : The size of the square

Usage:
    n_square = Square()

"""


class Square:
    """
    This is a class named square that defines size

    Attributes:
        ___size: the size of the square

    """
    def __init__(self, size=0):
        """
        Initialize a new instance of a square class

        Args:
            size (int): the size of the square

        Raises:
            TypeError: if size is not int
            ValueError: if value negative

        Returns:
            None
    """
        if type(size) is not int:

            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        else:
            self.__size = size
