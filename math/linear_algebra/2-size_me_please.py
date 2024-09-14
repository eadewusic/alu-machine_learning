#!/usr/bin/env python3

"""
2-size_me_please - Module for calculating the shape of a matrix.

This module contains the matrix_shape function which computes
the shape of a matrix as a list of integers.
"""


def matrix_shape(matrix):
    """
    Calculate the shape of a matrix.

    Args:
        matrix (list): A nested list representing the matrix.

    Returns:
        list: A list of integers representing the shape of the matrix.
    """
    shape = []
    while isinstance(matrix, list):
        shape.append(len(matrix))
        matrix = matrix[0]
    return shape
