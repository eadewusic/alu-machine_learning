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
            nx (int): Number of input features.
            nodes (int): Number of nodes in the hidden layer

        Raises:
            TypeError: If nx or nodes are not integers
            ValueError: If nx or nodes are less than 1
        """
        # Validate nx
        if not isinstance(nx, int):
            raise TypeError("nx must be an integer")
        if nx < 1:
            raise ValueError("nx must be a positive integer")

        # Validate nodes
        if not isinstance(nodes, int):
            raise TypeError("nodes must be an integer")
        if nodes < 1:
            raise ValueError("nodes must be a positive integer")

        # Initialize weights and biases
        self.W1 = np.random.randn(nodes, nx)  # Random normal initialization
        self.b1 = np.zeros((nodes, 1))        # Zero bias for hidden layer
        self.A1 = 0              # Placeholder for activation of hidden layer

        self.W2 = np.random.randn(1, nodes)  # Random normal initialization
        self.b2 = 0                          # Zero bias for output layer
        self.A2 = 0            # Placeholder for activation of output layer
