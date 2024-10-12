#!/usr/bin/env python3
"""
Binomial distribution class
"""


class Binomial:
    """
    Represents a Binomial distribution.

    A Binomial distribution is a discrete probability distribution
    of the number of successes in a sequence of n independent
    experiments. Each experiment results in a success with
    probability p.

    Attributes:
        n (int): Number of Bernoulli trials.
        p (float): Probability of success on each trial.

    Parameters:
        data (list, optional): A list of data points to estimate
                               the distribution parameters.
        n (int, optional): Number of Bernoulli trials (default is 1).
        p (float, optional): Probability of success (default is 0.5).

    Raises:
        ValueError: If n is not a positive value or if p is not in
                     the range (0, 1).
        TypeError: If data is not a list.
        ValueError: If data contains fewer than two values.
    """

    def __init__(self, data=None, n=1, p=0.5):
        if data is None:
            if n < 1:
                raise ValueError("n must be a positive value")
            else:
                self.n = n

            if p <= 0 or p >= 1:
                raise ValueError("p must be greater than 0 and less than 1")
            else:
                self.p = p
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            elif len(data) < 2:
                raise ValueError("data must contain multiple values")
            else:
                mean = float(sum(data) / len(data))
                summation = 0
                for x in data:
                    summation += ((x - mean) ** 2)
                variance = (summation / len(data))
                q = variance / mean
                p = (1 - q)
                n = round(mean / p)
                p = float(mean / n)
                self.n = n
                self.p = p

    def comb(self, n, k):
        """
        Calculates the binomial coefficient C(n, k).

        Parameters:
            n (int): Total number of trials.
            k (int): Number of successes.

        Returns:
            int: The binomial coefficient C(n, k).
        """
        if k < 0 or k > n:
            return 0
        if k == 0 or k == n:
            return 1

        # Calculate C(n, k) using an iterative approach
        k = min(k, n - k)  # Take advantage of symmetry
        c = 1
        for i in range(k):
            c = c * (n - i) // (i + 1)
        return c

    def pmf(self, k):
        """
        Calculates the PMF for a given number of successes.

        Parameters:
            k (int or float): The number of successes.

        Returns:
            float: The PMF value for k.
        """
        k = int(k)

        if k < 0 or k > self.n:
            return 0

        pmf_value = (self.comb(self.n, k) * (self.p ** k)
                     * ((1 - self.p) ** (self.n - k)))
        return pmf_value

    def cdf(self, k):
        """
        Calculates the CDF for a given number of successes.

        Parameters:
            k (int or float): The number of successes.

        Returns:
            float: The CDF value for k.
        """
        k = int(k)

        # If k is out of range, return 0
        if k < 0:
            return 0
        if k >= self.n:
            return 1

        # Calculate the CDF as the sum of PMF values
        cdf_value = sum(self.pmf(i) for i in range(k + 1))
        return cdf_value
