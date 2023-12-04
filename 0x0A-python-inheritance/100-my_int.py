#!/usr/bin/python3
"""
    Module defines MyInt class"
"""


class MyInt(int):
    """
        class that inherits from int

    """
    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        if isinstance(other, MyInt):
            return self.value != other.value
        return False

    def __ne__(self, other):
        return not self.__eq__(other)
