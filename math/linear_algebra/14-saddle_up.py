#!/usr/bin/env python3
"""
Module for performing matrix multiplication using numpy
"""

import numpy as np


def np_matmul(mat1, mat2):
    """
    Performs matrix multiplication of two numpy arrays

    Args:
        mat1 (numpy.ndarray): The first input numpy array
        mat2 (numpy.ndarray): The second input numpy array

    Returns:
        numpy.ndarray: The resulting numpy array after matrix multiplication
    """
    return np.matmul(mat1, mat2)
