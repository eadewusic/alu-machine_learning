#!/usr/bin/env python3

"""
Module for calculating the determinant of a matrix.
"""

def determinant(matrix):
    """
    Calculates the determinant of a matrix.

    :param matrix: list of lists whose determinant is to be calculated
    :return: the determinant of the matrix
    :raises TypeError: if matrix is not a list of lists
    :raises ValueError: if matrix is not a square matrix
    """
    # Check if matrix is a list of lists
    if not isinstance(
        matrix,
        list) or not all(
        isinstance(
            row,
            list) for row in matrix):
        raise TypeError("matrix must be a list of lists")

    # Check if matrix is empty (0x0 matrix is valid but [] alone is not)
    if matrix == []:
        raise TypeError("matrix must be a list of lists")

    # Handle the special case of 0x0 matrix
    if matrix == [[]]:
        return 1

    # Check if the matrix is square
    if any(len(row) != len(matrix) for row in matrix):
        raise ValueError("matrix must be a square matrix")

    # Base case: 1x1 matrix
    if len(matrix) == 1 and len(matrix[0]) == 1:
        return matrix[0][0]

    # Base case: 2x2 matrix
    if len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    # Recursive case for larger matrices (Laplace expansion)
    det = 0
    for i in range(len(matrix)):
        # Get the minor matrix
        minor = [row[:i] + row[i + 1:] for row in matrix[1:]]
        # Calculate the cofactor
        cofactor = ((-1) ** i) * matrix[0][i] * determinant(minor)
        # Add to the determinant
        det += cofactor

    return det
