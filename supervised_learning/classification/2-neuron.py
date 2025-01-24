#!/usr/bin/env python3
"""
This module defines the Neuron class, which represents a single neuron
performing binary classification. It includes a method for forward propagation
"""

import numpy as np


class Neuron:
    """Defines a single neuron performing binary classification"""

    def __init__(self, nx):
        """
        Initialize the Neuron

        Args:
            nx (int): The number of input features to the neuron

        Raises:
            TypeError: If nx is not an integer
            ValueError: If nx is less than 1
        """
        if not isinstance(nx, int):
            raise TypeError("nx must be an integer")
        if nx < 1:
            raise ValueError("nx must be positive")

        self.__W = np.random.randn(1, nx)  # Weight vector
        self.__b = 0  # Bias
        self.__A = 0  # Activated output

    @property
    def W(self):
        """Getter for the weights vector"""
        return self.__W

    @property
    def b(self):
        """Getter for the bias"""
        return self.__b

    @property
    def A(self):
        """Getter for the activated output"""
        return self.__A

    def forward_prop(self, X):
        """
        Calculates the forward propagation of the neuron

        Args:
            X (numpy.ndarray): Input data with shape (nx, m)
                               nx is the number of input features,
                               m is the number of examples

        Returns:
            numpy.ndarray: The activated output of the neuron (__A)
        """
        # Linear transformation
        Z = np.dot(self.__W, X) + self.__b
        # Sigmoid activation function
        self.__A = 1 / (1 + np.exp(-Z))
        return self.__A
