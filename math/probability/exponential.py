#!/usr/bin/env python3
"""
Exponential distribution class
"""


class Exponential:
    """
    Represents an Exponential distribution
    """

    def __init__(self, data=None, lambtha=1.):
        """
        Initializes the Exponential distribution
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
            self.lambtha = float(1 / (sum(data) / len(data)))

    def pdf(self, x):
        """
        Calculates the value of the PDF for a given time period
        """
        if x < 0:
            return 0

        # Apply the PDF formula for Exponential distribution
        return self.lambtha * (2.7182818285 ** (-self.lambtha * x))

    def cdf(self, x):
        """
        Calculates the value of the CDF for a given time period
        """
        if x < 0:
            return 0

        # Apply the CDF formula for Exponential distribution
        return 1 - (2.7182818285 ** (-self.lambtha * x))
