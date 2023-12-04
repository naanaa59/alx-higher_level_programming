#!/usr/bin/python3
"""
    this is a module for BaseGeometry class
"""


class BaseGeometry():
    """
    method: area
    method: integer_validator
    """
    def area(self):
        """
            raises an Exception with message area is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
            validates value
            raises TypeError if value is not integer
            raises ValueError if value <= 0
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """
        class Rectangle that inherits from BaseGeometry
    """
    def __init__(self, width, height):
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
