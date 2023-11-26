#!/usr/bin/python3
'''
    This module has a function named matrix_divide
     divides all elements of a matrix.
    It has 2 arguments : a matrix and a div
    a test file checks for different cases :
'''


def matrix_divided(matrix, div):
    '''
    Returns a matrix with divided elements of a matrix by a div

    Args:
        matrix: a list of lists
        div: a number different than 0
    Returns: a matrix with results
    '''
    res_matrix = []
    res_row = []
    if div == 0:
        raise ZeroDivisionError("division by zero")
    elif not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    elif not isinstance(matrix, list) or \
            not all(isinstance(row, list) for row in matrix) or \
            not all(isinstance(e, (int, float))
                    for row in matrix for e in row):
        raise TypeError("matrix must be a matrix (list of lists)\
                             of integers/floats")
    elif not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    else:
        for row in matrix:
            for element in row:
                res = round(element / div, 2)
                res_row.append(res)
            res_matrix.append(res_row)
            res_row = []
    return res_matrix
