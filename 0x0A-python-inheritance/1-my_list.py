#!/usr/bin/python3
"""
    This module had a method named print_sorted
"""


class MyList(list):
    """
        Class MyList that inherits from list

        Methods:
                print_sorted: public instance
    """
    def print_sorted(self):
        print(sorted(self))
