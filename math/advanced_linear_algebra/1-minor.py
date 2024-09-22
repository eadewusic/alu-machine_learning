#!/usr/bin/env python3

"""
Module for calculating the minor matrix of a given matrix.
"""


def minor(matrix):
    """
    Returns the minor of matrix
    """
    if not isinstance(matrix, list) or len(matrix) == 0\
       or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a list of lists")

    # Check if matrix is squares
    n = len(matrix)
    if any(len(row) != n for row in matrix):
        raise ValueError("matrix must be a non-empty square matrix")

    def submatrix(mat, i, j):
        return [row[:j] + row[j + 1:] for row in (mat[:i] + mat[i + 1:])]

    def determinant(mat):
        if len(mat) == 1:
            return mat[0][0]
        if len(mat) == 2:
            return mat[0][0] * mat[1][1] - mat[0][1] * mat[1][0]
        det = 0
        for j in range(len(mat)):
            det += ((-1) ** j) * mat[0][j] * determinant(submatrix(mat, 0, j))
        return det

    if n == 1:
        return [[1]]

    minor_matrix = []
    for i in range(n):
        minor_row = []
        for j in range(n):
            minor_row.append(determinant(submatrix(matrix, i, j)))
        minor_matrix.append(minor_row)

    return minor_matrix
