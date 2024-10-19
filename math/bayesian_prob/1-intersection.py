#!/usr/bin/env python3
"""
Intersection function for calculating likelihood
with prior beliefs
"""

import numpy as np


def intersection(x, n, P, Pr):
    """
    Calculates the intersection of obtaining the data
    with various hypothetical probabilities

    Args:
        x (int): The number of patients that develop severe side effects
        n (int): The total number of patients observed
        P (numpy.ndarray): 1D array of hypothetical probabilities
        Pr (numpy.ndarray): 1D array of prior beliefs

    Raises:
        ValueError: If n is not a positive integer, x is not >= 0, or x > n
        TypeError: If P is not a 1D numpy.ndarray or Pr
        does not match the shape of P
        ValueError: If any value in P or Pr is not in the range [0, 1]
        ValueError: If Pr does not sum to 1

    Returns:
        numpy.ndarray: 1D array containing the intersection of
        obtaining x and n with each probability in P
    """

    # Validate input parameters
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer")

    if not isinstance(x, int) or x < 0:
        raise ValueError(
            "x must be an integer that is greater than or equal to 0")

    if x > n:
        raise ValueError("x cannot be greater than n")

    if not isinstance(P, np.ndarray) or P.ndim != 1:
        raise TypeError("P must be a 1D numpy.ndarray")

    if not isinstance(Pr, np.ndarray) or Pr.shape != P.shape:
        raise TypeError("Pr must be a numpy.ndarray with the same shape as P")

    if np.any((P < 0) | (P > 1)):
        raise ValueError("All values in P must be in the range [0, 1]")

    if np.any((Pr < 0) | (Pr > 1)):
        raise ValueError("All values in Pr must be in the range [0, 1]")

    if not np.isclose(np.sum(Pr), 1):
        raise ValueError("Pr must sum to 1")

    # Calculate likelihood
    factorial_n = np.math.factorial(n)
    factorial_x = np.math.factorial(x)
    factorial_n_x = np.math.factorial(n - x)

    likelihood_values = (P ** x) * ((1 - P) ** (n - x)) * \
        (factorial_n / (factorial_x * factorial_n_x))

    # Calculate intersection
    intersection_values = likelihood_values * Pr

    return intersection_values
