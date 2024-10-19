#!/usr/bin/env python3
"""
Defines a function that calculates the posterior probability
that the probability of developing severe side effects falls
within a specific range given the data
"""

from scipy import special

def posterior(x, n, p1, p2):
    """
    Calculates the posterior probability that the probability of developing
    severe side effects falls within the range [p1, p2] given the data

    Parameters:
        x (int): Number of patients that develop severe side effects
        n (int): Total number of patients observed
        p1 (float): Lower bound of the range
        p2 (float): Upper bound of the range

    Returns:
        float: The posterior probability that p is within the range [p1, p2]
    """

    # Input validation
    if type(n) is not int or n <= 0:
        raise ValueError("n must be a positive integer")
    if type(x) is not int or x < 0:
        raise ValueError("x must be an integer that is greater than or equal to 0")
    if x > n:
        raise ValueError("x cannot be greater than n")
    
    # Validate p1 and p2
    for p, name in zip([p1, p2], ["p1", "p2"]):
        if not isinstance(p, float) or p < 0 or p > 1:
            raise ValueError(f"{name} must be a float in the range [0, 1]")
    
    if p2 <= p1:
        raise ValueError("p2 must be greater than p1")

    # Calculate the posterior probability using the Beta distribution
    alpha = x + 1
    beta = n - x + 1

    # CDF for Beta distribution to calculate P(p1 < p < p2)
    prob_p2 = special.btdtr(alpha, beta, p2)  # P(p < p2)
    prob_p1 = special.btdtr(alpha, beta, p1)  # P(p < p1)

    # The posterior probability is the difference between the two CDFs
    posterior_prob = prob_p2 - prob_p1

    return posterior_prob
