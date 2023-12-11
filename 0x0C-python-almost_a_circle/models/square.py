#!/usr/bin/python3
"""
    This module defines a class Square that inherits from Rectangle
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
        Inherits from class Rectangle
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
            Init method for Square
        """
        super().__init__(width=size, height=size, x=x, y=y, id=id)

    def __str__(self):
        """
            str method for Square
        """
        return "[Square] ({}) {}/{} - {}".format(
                self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """ getter for the size """
        return self.width

    @size.setter
    def size(self, value):
        """ setter for the size """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.width = value
            self.height = value

    def update(self, *args, **kwargs):
        """ update the attributes """
        attr_names = ['id', 'size', 'x', 'y']
        if args:

            for i, arg in enumerate(args):
                setattr(self, attr_names[i], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
            Returns the dictionary representation of a Square object
        """
        square_dict = super().to_dictionary()
        square_dict['size'] = self.size
        square_dict.pop('width')
        square_dict.pop('height')
        return square_dict
