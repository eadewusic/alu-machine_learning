#!/usr/bin/env python3
"""
Normal distribution class
"""


class Normal:
    """Represents a Normal distribution"""

    def __init__(self, data=None, mean=0., stddev=1.):
        """Initializes the Normal distribution

        Args:
            data (list, optional): A list of data points. If provided, the mean
                and standard deviation will be calculated from the data
            mean (float, optional): mean of the distribution. Defaults to 0.
            stddev (float, optional): standard deviation of the distribution
                Defaults to 1.
        """
        if data is None:
            # Validate stddev
            if stddev < 1:
                raise ValueError("stddev must be a positive value")
            self.stddev = float(stddev)
            self.mean = float(mean)
        else:
            # Validate data
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")

            # Calculate mean and standard deviation from data
            self.mean = sum(data) / len(data)
            summation = 0
            for x in data:
                summation += ((x - self.mean) ** 2)
            self.stddev = (summation / len(data)) ** (1 / 2)

    def z_score(self, x):
        """Calculates the z-score of a given x-value

        Args:
            x (float): The x-value.

        Returns:
            float: The z-score of x.
        """
        return (x - self.mean) / self.stddev

    def x_value(self, z):
        """Calculates the x-value of a given z-score

        Args:
            z (float): The z-score

        Returns:
            float: The x-value corresponding to the z-score
        """
        return (z * self.stddev) + self.mean

    def pdf(self, x):
        """Calculates the value of the PDF for a given x-value

        Args:
            x (float): The x-value

        Returns:
            float: The probability density function (PDF) value for x
        """
        e = 2.7182818285
        pi = 3.1415926536
        power = -0.5 * (self.z_score(x) ** 2)
        coefficient = 1 / (self.stddev * ((2 * pi) ** (1 / 2)))
        return coefficient * (e ** power)

    def cdf(self, x):
        """Calculates the value of the CDF for a given x-value

        Args:
            x (float): The x-value

        Returns:
            float: The cumulative distribution function (CDF) value for x
        """
        pi = 3.1415926536
        value = (x - self.mean) / (self.stddev * (2 ** (1 / 2)))
        erf = value - ((value ** 3) / 3) + ((value ** 5) / 10)
        erf = erf - ((value ** 7) / 42) + ((value ** 9) / 216)
        erf *= (2 / (pi ** (1 / 2)))
        return (1 / 2) * (1 + erf)
