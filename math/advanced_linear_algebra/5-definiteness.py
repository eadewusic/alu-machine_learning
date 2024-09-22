#!/usr/bin/env python3

"""
Module for calculating the definiteness of a symmetric matrix.
The module provides a function to determine if a given numpy.ndarray matrix
is positive definite, positive semi-definite, negative semi-definite,
negative definite, or indefinite.
"""

import numpy as np


def definiteness(matrix):
    """
    Determines the definiteness of a symmetric matrix.

    Args:
        matrix (numpy.ndarray): The input square matrix to evaluate.

    Returns:
        str: A string indicating the type of definiteness ("Positive definite",
             "Positive semi-definite", "Negative definite", "Negative semi-definite",
             "Indefinite") or None if the matrix is not valid or not symmetric.

    Raises:
        TypeError: If the input is not a numpy.ndarray.
    """
    if not isinstance(matrix, np.ndarray):
        raise TypeError("matrix must be a numpy.ndarray")

    if matrix.ndim != 2 or matrix.shape[0] != matrix.shape[1] or matrix.size == 0:
        return None

    # Check if the matrix is symmetric
    if not np.array_equal(matrix, matrix.T):
        return None

    eigenvalues = np.linalg.eigvals(matrix)

    if np.all(eigenvalues > 0):
        return "Positive definite"
    elif np.all(eigenvalues >= 0):
        return "Positive semi-definite"
    elif np.all(eigenvalues < 0):
        return "Negative definite"
    elif np.all(eigenvalues <= 0):
        return "Negative semi-definite"
    else:
        return "Indefinite"
