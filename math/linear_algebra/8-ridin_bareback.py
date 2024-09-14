#!/usr/bin/env python3

"""
8-ridin_bareback - Module for performing matrix multiplication

This module contains the mat_mul function which multiplies
two 2D matrices
"""


def mat_mul(mat1, mat2):
    """
    Multiply two 2D matrices.

    Args:
        mat1 (list of list): The first matrix (m x n)
        mat2 (list of list): The second matrix (n x p)

    Returns:
        list of list: A new matrix resulting from the multiplication
                      of mat1 and mat2 - Returns None if the matrices
                      cannot be multiplied
    """
    # Check if matrices can be multiplied
    if len(mat1[0]) != len(mat2):
        return None

    # Create the result matrix with the appropriate dimensions
    result = [[0] * len(mat2[0]) for _ in range(len(mat1))]

    # Perform matrix multiplication
    for i in range(len(mat1)):
        for j in range(len(mat2[0])):
            result[i][j] = sum(mat1[i][k] * mat2[k][j]
                               for k in range(len(mat2)))

    return result
