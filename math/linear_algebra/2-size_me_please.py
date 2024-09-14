#!/usr/bin/env python3

def matrix_shape(matrix):
    """
    Calculates the shape (dimensions) of a matrix.

    Args:
        matrix: A 2D or higher dimensional list representing a matrix.

    Returns:
        A list of integers representing the shape of the matrix.
    """

    # Check if it's a 1D list
    if not isinstance(matrix, list):
        return [1]  # Handle single element (not a list)

    # Get the shape of the first row for 2D or higher dimensional lists
    shape = list(len(row) for row in matrix[:1])

    return shape
