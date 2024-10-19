#!/usr/bin/env python3
"""
This module provides a function to calculate
the correlation matrix from a covariance matrix
"""

import numpy as np


def correlation(C):
    """
    Calculates the correlation matrix from a covariance matrix

    Parameters:
    C (numpy.ndarray): A 2D square covariance matrix of shape (d, d)

    Returns:
    numpy.ndarray: A 2D square correlation matrix of shape (d, d)

    Raises:
    TypeError: If C is not a numpy.ndarray
    ValueError: If C is not a 2D square matrix
    """
    # Check if C is a numpy.ndarray
    if not isinstance(C, np.ndarray):
        raise TypeError("C must be a numpy.ndarray")

    # Check if C is a 2D square matrix
    if C.ndim != 2 or C.shape[0] != C.shape[1]:
        raise ValueError("C must be a 2D square matrix")

    # Calculate the standard deviations
    stddevs = np.sqrt(np.diag(C))

    # Avoid division by zero for any standard deviations that are zero
    with np.errstate(invalid='ignore'):
        corr = C / np.outer(stddevs, stddevs)

    # Replace any NaN values (resulting from division by zero) with 0
    corr = np.nan_to_num(corr)

    return corr
