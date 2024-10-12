#!/usr/bin/env python3
"""
Normal distribution class
"""


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
        return variance ** 0.5  # Standard deviation is the square root of variance
