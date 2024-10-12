#!/usr/bin/env python3
"""
Normal distribution class
"""

import math

class Exponential:
    """Represents an Exponential distribution"""

    def __init__(self, data=None, lambtha=1.):
        """Initializes the Exponential distribution"""
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
        """Calculates the value of the PDF for a given time period"""
        if x < 0:
            return 0
        return self.lambtha * (self.lambtha ** x) * (math.e ** (-self.lambtha * x))

    def cdf(self, x):
        """Calculates the value of the CDF for a given time period"""
        if x < 0:
            return 0
        return 1 - (math.e ** (-self.lambtha * x))


class Normal:
    """Represents a Normal distribution"""

    def __init__(self, data=None, mean=0., stddev=1.):
        """Initializes the Normal distribution"""
        if data is None:
            if stddev <= 0:
                raise ValueError("stddev must be a positive value")
            self.mean = float(mean)
            self.stddev = float(stddev)
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            self.mean = self.calculate_mean(data)
            self.stddev = self.calculate_stddev(data, self.mean)

    def calculate_mean(self, data):
        """Calculate the mean of a list of numbers"""
        return sum(data) / len(data)

    def calculate_stddev(self, data, mean):
        """Calculate the standard deviation of a list of numbers"""
        variance = sum((x - mean) ** 2 for x in data) / len(data)
        # Standard deviation is the square root of variance
        return variance ** 0.5

    def z_score(self, x):
        """Calculates the z-score of a given x-value"""
        return (x - self.mean) / self.stddev

    def x_value(self, z):
        """Calculates the x-value of a given z-score"""
        return self.mean + z * self.stddev

    def pdf(self, x):
        """Calculates the value of the PDF for a given x-value"""
        if self.stddev <= 0:
            raise ValueError("stddev must be a positive value")
        exponent = -((x - self.mean) ** 2) / (2 * (self.stddev ** 2))
        return (1 / (self.stddev * (2 * math.pi) ** 0.5)) * (math.e ** exponent)

    def cdf(self, x):
        """Calculates the value of the CDF for a given x-value"""
        if self.stddev <= 0:
            raise ValueError("stddev must be a positive value")
        z = self.z_score(x)  # Calculate z-score
        return 0.5 * (1 + math.erf(z / math.sqrt(2)))  # CDF using the error function
