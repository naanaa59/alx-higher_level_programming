#!/usr/bin/python3
"""
    pascal_triangle method
"""


def pascal_triangle(n):
    """
        returns a list of lists of integers
    """
    list_int = []
    list_all = []
    list_tmp = []
    if n <= 0:
        return list_all
    list_all = [[1]]
    for row in range(n - 1):
        list_int = list_all[-1]
        list_tmp = [1]
        for i in range(len(list_int) - 1):
            list_tmp.append(list_int[i] + list_int[i + 1])
        list_tmp.append(1)
        list_all.append(list_tmp)
    return list_all
