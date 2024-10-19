#!/usr/bin/env python3
"""
Posterior probability function for calculating
the posterior of obtaining data
"""

import numpy as np


def posterior(x, n, P, Pr):
    """
    Calculates the posterior probability for the
    various hypothetical probabilities of developing severe side effects
    given the data

    Parameters:
        x (int): Total number of patients that develop severe side effects
        n (int): Total number of patients observed
        P (1D numpy.ndarray): Array containing various hypothetical probabilities
        of developing severe side effects
        Pr (1D numpy.ndarray): Array containing the prior beliefs of P
    Returns:
        numpy.ndarray: The posterior probability of each
        probability in P, given x and n
    """
    # Input validation
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer")
    if not isinstance(x, int) or x < 0:
        raise ValueError(
            "x must be an integer that is greater than or equal to 0")
    if x > n:
        raise ValueError("x cannot be greater than n")
    if not isinstance(P, np.ndarray) or len(P.shape) != 1:
        raise TypeError("P must be a 1D numpy.ndarray")
    if not isinstance(Pr, np.ndarray) or Pr.shape != P.shape:
        raise TypeError("Pr must be a numpy.ndarray with the same shape as P")

    # Check values in P and Pr
    for value in range(P.shape[0]):
        if P[value] > 1 or P[value] < 0:
            raise ValueError("All values in P must be in the range [0, 1]")
        if Pr[value] > 1 or Pr[value] < 0:
            raise ValueError("All values in Pr must be in the range [0, 1]")

    # Check that Pr sums to 1
    if not np.isclose(np.sum(Pr), 1):
        raise ValueError("Pr must sum to 1")

    # Likelihood calculated as binomial distribution
    factorial = np.math.factorial
    fact_coefficient = factorial(n) / (factorial(n - x) * factorial(x))
    likelihood = fact_coefficient * (P ** x) * ((1 - P) ** (n - x))

    # Intersection is the likelihood times priors
    intersection = likelihood * Pr

    # Marginal probability is the sum over all probabilities of events
    marginal = np.sum(intersection)

    # Posterior probability is the intersection divided by marginal probability
    posterior = intersection / marginal

    return posterior
