#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    square_matrix = []
    square_list = []
    for i in range(len(matrix)):
        square_list = list(map(lambda x: x ** 2, matrix[i]))
        square_matrix.append(square_list)
    return square_matrix
