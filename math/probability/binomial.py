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
        # Check if data is provided
        if data is None:
            # If no data is provided, check the validity of n
            if n < 1:
                raise ValueError("n must be a positive value")
            else:
                self.n = n  # Set the number of trials n

            # Check the validity of p
            if p <= 0 or p >= 1:
                raise ValueError("p must be greater than 0 and less than 1")
            else:
                self.p = p  # Set the probability of success p
        else:
            # If data is provided, validate the data type
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            elif len(data) < 2:
                raise ValueError("data must contain multiple values")
            else:
                # Calculate the mean of the data
                mean = float(sum(data) / len(data))
                summation = 0

                # Calculate the variance of the data
                for x in data:
                    summation += ((x - mean) ** 2)
                variance = (summation / len(data))

                # Calculate q and derive p from variance and mean
                q = variance / mean
                p = (1 - q)  # Calculate probability of success

                # Estimate the number of trials n and recalculate p
                n = round(mean / p)
                p = float(mean / n)

                # Set the instance attributes for n and p
                self.n = n  # Number of trials
                self.p = p  # Probability of success
