#!/usr/bin/env python3
"""
Module for transposing a matrix
"""


def np_transpose(matrix):
    """
    Transposes a 2D list matrix

    Args:
        matrix (list of list): The input 2D list matrix

    Returns:
        list of list: The transposed matrix.
    """
    # Transpose using list comprehension and zip
    return [list(row) for row in zip(*matrix)]
