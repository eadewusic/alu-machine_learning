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
        list of list: The transposed matrix
    """
    if not matrix or not isinstance(
            matrix,
            list) or not isinstance(
            matrix[0],
            list):
        return []

    transposed = list(map(list, zip(*matrix)))
    return transposed
