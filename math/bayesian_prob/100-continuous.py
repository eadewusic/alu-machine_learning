#!/usr/bin/env python3
"""
Defines a function that calculates the posterior probability that the
various hypothetical probabilities of developing severe side effects
falls within a specific range given the data
"""

from scipy import special


def posterior(x, n, p1, p2):
    """
    Calculates the posterior probability that the
    various hypothetical probabilities of developing severe side effects
    falls within a specific range given the data

    Parameters:
        x [int]: total number of patients that develop severe side effects
        n [int]: total number of patients observed
        p1 [float]: the lower bound on the range
        p2 [float]: the upper bound on the range

    Prior beliefs of p follow a uniform distribution

    Returns:
        the posterior probability that p is within
        range [p1, p2] given x and n
    """
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer")
    if not isinstance(x, int) or x < 0:
        raise ValueError(
            "x must be an integer that is greater than or equal to 0")
    if x > n:
        raise ValueError("x cannot be greater than n")
    if not isinstance(p1, float) or p1 < 0 or p1 > 1:
        raise ValueError("p1 must be a float in the range [0, 1]")
    if not isinstance(p2, float) or p2 < 0 or p2 > 1:
        raise ValueError("p2 must be a float in the range [0, 1]")
    if p2 <= p1:
        raise ValueError("p2 must be greater than p1")

    # Use p and (1 - p) or in our case x and (n - x) for the data
    # Add uniformly distributed priors with +1 in parameters
    # Cumulative distribution function for beta distribution for 0 to p1
    beta_dist1 = special.btdtr(x + 1, n - x + 1, p1)
    # Cumulative distribution function for beta distribution for 0 to p2
    beta_dist2 = special.btdtr(x + 1, n - x + 1, p2)
    # Subtract to get the difference between p2 and p1
    posterior = beta_dist2 - beta_dist1
    return posterior
