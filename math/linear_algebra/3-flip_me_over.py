#!/usr/bin/env python3

"""
3-flip_me_over - Module for transposing a 2D matrix.

This module contains the matrix_transpose function which computes
the transpose of a 2D matrix.
"""


def matrix_transpose(matrix):
    """
    Calculate the transpose of a 2D matrix.

    Args:
        matrix (list of lists):
        A 2D list representing the matrix to be transposed.

    Returns:
        list of lists: A new 2D list representing the transposed matrix.
    """
    return [list(row) for row in zip(*matrix)]
