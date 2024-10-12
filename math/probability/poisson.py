#!/usr/bin/env python3
"""
Poisson distribution class
"""


class Poisson:
    """
    Represents a Poisson distribution
    """

    def __init__(self, data=None, lambtha=1.):
        """
        Initializes the Poisson distribution
        """
        if data is None:
            if lambtha <= 0:
                raise ValueError("lambtha must be a positive value")
            self.lambtha = float(lambtha)
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            self.lambtha = float(sum(data) / len(data))

    def pmf(self, k):
        """
        Calculates the value of the PMF
        for a given number of occurrences (k)
        """
        if k < 0:
            return 0

        k = int(k)  # Ensure k is an integer

        # Helper function to calculate factorial
        def factorial(n):
            if n == 0 or n == 1:
                return 1
            result = 1
            for i in range(2, n + 1):
                result *= i
            return result

        # Apply the PMF formula for Poisson distribution
        e = 2.7182818285  # Euler's number
        lambtha = self.lambtha
        return (lambtha ** k) * (e ** (-lambtha)) / factorial(k)

    def cdf(self, k):
        """
        Calculates the value of the CDF for a
        given number of successes (k)
        """
        if k < 0:
            return 0

        k = int(k)  # Ensure k is an integer

        # Sum the PMFs from 0 to k
        cumulative_prob = 0
        for i in range(k + 1):
            cumulative_prob += self.pmf(i)

        return cumulative_prob
