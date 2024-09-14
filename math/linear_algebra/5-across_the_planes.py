#!/usr/bin/env python3

"""
5-across_the_planes - Module for element-wise addition of two 2D matrices

This module contains the add_matrices2D function
which adds two 2D matrices element-wise
"""


def add_matrices2D(mat1, mat2):
    """
    Add two 2D matrices element-wise.

    Args:
        mat1 (list of lists): The first 2D list of integers or floats
        mat2 (list of lists): The second 2D list of integers or floats

    Returns:
        list of lists or None: A new 2D list containing the element-wise
                               sum of mat1 and mat2, or None if mat1
                               and mat2 are not the same shape
    """
    if len(mat1) != len(mat2) or any(len(row1) != len(row2)
                                     for row1, row2 in zip(mat1, mat2)):
        return None
    return [[x + y for x, y in zip(row1, row2)]
            for row1, row2 in zip(mat1, mat2)]
