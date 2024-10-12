#!/usr/bin/env python3
"""
Normal distribution class
"""

import math


class Normal:
    def __init__(self, data=None, mean=0., stddev=1.):
        if data is None:
            if stddev < 1:
                raise ValueError("stddev must be a positive value")
            else:
                self.stddev = float(stddev)
                self.mean = float(mean)
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            elif len(data) < 2:
                raise ValueError("data must contain multiple values")
            else:
                mean = float(sum(data) / len(data))
                self.mean = mean
                summation = 0
                for x in data:
                    summation += ((x - mean) ** 2)
                stddev = (summation / len(data)) ** (1 / 2)
                self.stddev = stddev

    def z_score(self, x):
        return (x - self.mean) / self.stddev

    def x_value(self, z):
        return (z * self.stddev) + self.mean

    def pdf(self, x):
        e = 2.7182818285
        pi = 3.1415926536
        power = -0.5 * (self.z_score(x) ** 2)
        coefficient = 1 / (self.stddev * ((2 * pi) ** (1 / 2)))
        return coefficient * (e ** power)

    def cdf(self, x):
        pi = 3.1415926536
        value = (x - self.mean) / (self.stddev * (2 ** (1 / 2)))
        erf = value - ((value ** 3) / 3) + ((value ** 5) / 10)
        erf = erf - ((value ** 7) / 42) + ((value ** 9) / 216)
        erf *= (2 / (pi ** (1 / 2)))
        return (1 / 2) * (1 + erf)
