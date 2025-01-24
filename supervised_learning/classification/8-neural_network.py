#!/usr/bin/env python3
"""
This module defines the NeuralNetwork class, which represents a neural network
with one hidden layer performing binary classification
"""

import numpy as np


class NeuralNetwork:
    """
    Represents a neural network with one hidden
    layer performing binary classification
    """

    def __init__(self, nx, nodes):
        """
        Initialize the NeuralNetwork

        Args:
            nx (int): Number of input features
            nodes (int): Number of nodes in the hidden layer

        Raises:
            TypeError: If nx or nodes are not integers
            ValueError: If nx or nodes are less than 1
        """
        if not isinstance(nx, int):
            raise TypeError("nx must be an integer")
        if nx < 1:
            raise ValueError("nx must be a positive integer")
        if not isinstance(nodes, int):
            raise TypeError("nodes must be an integer")
        if nodes < 1:
            raise ValueError("nodes must be a positive integer")

        # Initialize hidden layer parameters
        self.W1 = np.random.randn(nodes, nx)  # Weights for hidden layer
        self.b1 = np.zeros((nodes, 1))        # Bias for hidden layer
        self.A1 = 0                # Activated output of hidden layer

        # Initialize output layer parameters
        self.W2 = np.random.randn(1, nodes)  # Weights for output layer
        self.b2 = 0                          # Bias for output layer
        self.A2 = 0                          # Activated output of output layer
