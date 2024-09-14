#!/usr/bin/env python3

"""
7-gettin_cozy - Module for concatenating two 2D matrices
along a specified axis

This module contains the cat_matrices2D function
which concatenates two 2D matrices
"""


def cat_matrices2D(mat1, mat2, axis=0):
    """
    Concatenate two 2D matrices along a specified axis

    Args:
        mat1 (list of list): The first matrix to concatenate.
        mat2 (list of list): The second matrix to concatenate.
        axis (int): The axis along which to concatenate (0 for rows, 1 for columns)

    Returns:
        list of list: A new matrix resulting from the concatenation of mat1 and mat2
                      Returns None if the matrices cannot be concatenated
    """
    if axis == 0:
        if len(mat1[0]) != len(mat2[0]):
            return None
        return mat1 + mat2
    elif axis == 1:
        if len(mat1) != len(mat2):
            return None
        return [r1 + r2 for r1, r2 in zip(mat1, mat2)]
    else:
        return None
