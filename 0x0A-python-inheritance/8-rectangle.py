#!/usr/bin/python3
"""
    this is a module for BaseGeometry class
"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """
        class Rectangle that inherits from BaseGeometry
    """
    def __init__(self, width, height):
        """
            init function class Rectangle
        """

        super().integer_validator("width", width)
        self.__width = width

        super().integer_validator("height", height)
        self.__height = height
