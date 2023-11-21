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
    def __init__(self, size):
        """
        Initialize a new instance of a square class

        Args:
            size: the size of the square

        Returns:
            None
    """
        self.__size = size
