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
        __size: the size of the square
        __position: a tuple with 2 positive values

    """
    def __init__(self, size=0, position=(0, 0)):
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
        if type(position) is not tuple or len(position) != 2\
           or type(position[0]) is not int or type(position[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")

        else:
            self.__size = size
            self.__position = position

    def area(self):

        """
        calculates the area of a current square

        Retunrs:
            the current square area
        """
        return self.__size ** 2

    @property
    def size(self):
        """
        gets the size object

        Returns:
            the size object
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        sets the size of a square
        """
        if type(value) is not int:

            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

        else:
            self.__size = value

    def my_print(self):
        """
        prints in stdout the square with #

        Args:
            None
        Returns:
            None
        """
        size = self.size
        position = self.position
        if size == 0:
            print()
        else:
            for y in range(position[1]):
                print()
            for i in range(size):
                for x in range(position[0]):
                    print(" ", end="")
                for j in range(size):
                    print("#", end="")
                print()

    @property
    def position(self):
        """
        gets the position of the square

        Returns:
            The position of the square
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        sets a position with 2 positive values

        Args:
            value: a tuple with 2 positive digits
        Returns:
            None
        """
        if type(value) is not tuple or len(value) != 2\
           or type(value[0]) is not int or type(value[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value
