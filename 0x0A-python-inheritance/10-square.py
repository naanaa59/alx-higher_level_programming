#!/usr/bin/python3
"""
    module defines square class
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
        class square that inherits from Rectangle
    """
    def __init__(self, size):
        super().integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        return super().area()
