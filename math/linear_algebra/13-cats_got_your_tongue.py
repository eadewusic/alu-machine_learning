#!/usr/bin/env python3
"""
Module for concatenating two numpy arrays along a specific axis
"""


def np_cat(mat1, mat2, axis=0):
    """
    Concatenates two numpy arrays along the specified axis

    Args:
        mat1 (numpy.ndarray): The first input numpy array
        mat2 (numpy.ndarray): The second input numpy array
        axis (int): The axis along which the arrays will be concatenated (default is 0)

    Returns:
        numpy.ndarray: A new numpy array that is the result of
        concatenating mat1 and mat2 along the specified axis
    """
    return np.concatenate((mat1, mat2), axis=axis)
