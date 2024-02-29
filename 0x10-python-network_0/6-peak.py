#!/usr/bin/python3
"""
    This is a technical interview to find a peak in a list
"""


def find_peak(list_of_integers):
    """ This is the method finding the peak """
    if not list_of_integers:
        return None
    list_of_integers.sort()
    return list_of_integers[-1]
