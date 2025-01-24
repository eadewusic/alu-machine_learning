#!/usr/bin/env python3
"""
This module defines the Neuron class, which represents a single neuron
performing binary classification. The class is initialized with a number of
input features and defines public instance attributes for the weights, bias,
and activated output of the neuron
"""

import numpy as np


class Neuron:
    """
    Defines a single neuron performing binary classification
    """

    def __init__(self, nx):
        """
        Class constructor

        Parameters:
        nx (int): Number of input features to the neuron

        Raises:
        TypeError: If nx is not an integer
        ValueError: If nx is less than 1
        """
        if not isinstance(nx, int):
            raise TypeError("nx must be an integer")
        if nx < 1:
            raise ValueError("nx must be a positive integer")

        # Weights vector initialized with random normal distribution
        self.W = np.random.randn(1, nx)
        self.b = 0  # Bias initialized to 0
        self.A = 0  # Activated output initialized to 0
