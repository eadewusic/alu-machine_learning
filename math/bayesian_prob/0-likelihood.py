#!/usr/bin/env python3
"""
Likelihood function for binomial distribution data analysis
"""

import numpy as np


def likelihood(x, n, P):
    """
    Calculates the likelihood of obtaining data given
    various hypothetical probabilities

    Args:
        x (int): The number of patients that develop severe side effects
        n (int): The total number of patients observed
        P (numpy.ndarray): 1D array of hypothetical probabilities

    Raises:
        ValueError: If n is not a positive integer, x is not >= 0, or x > n
        TypeError: If P is not a 1D numpy.ndarray
        ValueError: If any value in P is not in the range [0, 1]

    Returns:
        numpy.ndarray: 1D array containing the likelihood
        of obtaining the data for each probability in P
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

    if np.any((P < 0) | (P > 1)):
        raise ValueError("All values in P must be in the range [0, 1]")

    # Calculate the likelihood using the binomial distribution
    factorial_n = np.math.factorial(n)
    factorial_x = np.math.factorial(x)
    factorial_n_x = np.math.factorial(n - x)

    likelihood_values = (P ** x) * ((1 - P) ** (n - x)) * \
        (factorial_n / (factorial_x * factorial_n_x))

    return likelihood_values
