#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix is None:
        return []
    return [[num ** 2 for num in row] for row in matrix]
