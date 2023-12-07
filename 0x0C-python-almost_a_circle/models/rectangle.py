#!/usr/bin/python3
"""
    This module has a class named Rectangle
"""
from models.base import Base


class Rectangle(Base):
    """
        This class named Rectangle inherits from Base
        Private instance attribute:
            __width -> width
            __height -> height
            __x -> x
            __y -> y
        Class constructor: def __init__
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
            initiation for the class Rectangle
        """
        if not isinstance(width, int) :
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = width

        if not isinstance(height, int) :
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = height

        if not isinstance(x, int) :
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = x

        if not isinstance(y, int) :
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = y

        super().__init__(id)

    """ Getter of the width """
    @property
    def width(self):
        return self.__width

    """ Setter for the width"""
    @width.setter
    def width(self, value):
        if not isinstance(value, int) :
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value


    """ Getter of the height """
    @property
    def height(self):
        return self.__height

    """ Setter for the height"""
    @height.setter
    def height(self, value):
        if not isinstance(value, int) :
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    """ Getter of the x """
    @property
    def x(self):
        return self.__x

    """ Setter for the height"""
    @x.setter
    def x(self, value):
        if not isinstance(value, int) :
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    """ Getter of the y """
    @property
    def y(self):
        return self.__y

    """ Setter for the y """
    @y.setter
    def y(self, value):
        if not isinstance(value, int) :
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value
