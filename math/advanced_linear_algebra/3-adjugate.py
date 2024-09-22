#!/usr/bin/env python3

"""
Module for calculating the adjugate matrix of a given matrix.
"""


def adjugate(matrix):
    """
    Returns the adjugate of the matrix.
    """
    if not isinstance(matrix, list) or len(matrix) == 0 \
       or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a list of lists")

    # Check if the matrix is square
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

    adjugate_matrix = []
    for i in range(n):
        adjugate_row = []
        for j in range(n):
            sign = (-1) ** (i + j)
            minor = determinant(submatrix(matrix, i, j))
            adjugate_row.append(sign * minor)
        adjugate_matrix.append(adjugate_row)

    # Transpose the cofactor matrix to get the adjugate
    adjugate_matrix = [list(row) for row in zip(*adjugate_matrix)]

    # Handle 1x1 case explicitly
    if n == 1:
        return [[1]]  # The adjugate of a 1x1 matrix is 1

    return adjugate_matrix
