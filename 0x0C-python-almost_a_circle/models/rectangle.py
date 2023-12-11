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
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = width

        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = height

        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = x

        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = y

        super().__init__(id)

    """ Getter of the width """
    @property
    def width(self):
        ''' getter for width '''
        return self.__width

    @width.setter
    def width(self, value):
        """ Setter for the width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """ Getter of the height """
        return self.__height

    @height.setter
    def height(self, value):
        """ Setter for the height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """ Getter of the x """
        return self.__x

    @x.setter
    def x(self, value):
        """ Setter for the height"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """ Getter of the y """
        return self.__y

    @y.setter
    def y(self, value):
        """ Setter for the y """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """ area method that calculates the area of a rectangle """
        return self.__width * self.__height

    def display(self):
        """ display method : displays the rectangle wit # """
        for k in range(self.__y):
            print()
        for j in range(self.__height):
            for m in range(self.__x):
                print(" ", end="")
            for i in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """ str gets the printable rectangle object """
        return "[Rectangle] ({}) {}/{} - {}/{}".
        format(self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """ update the attributes """
        attr_names = ['id', 'width', 'height', 'x', 'y']
        if args:

            for i, arg in enumerate(args):
                setattr(self, attr_names[i], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
            Returns a dictionary representation of the Rectangle object
        """
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }
