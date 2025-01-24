#!/usr/bin/env python3
"""
Defines the NeuralNetwork class for binary classification with one hidden layer.
"""

import numpy as np


class NeuralNetwork:
    """
    Represents a neural network with one hidden layer performing binary classification.
    """

    def __init__(self, nx, nodes):
        """
        Initialize the neural network.

        Args:
            nx (int): Number of input features.
            nodes (int): Number of nodes in the hidden layer.

        Raises:
            TypeError: If nx or nodes are not integers.
            ValueError: If nx or nodes are less than 1.
        """
        if not isinstance(nx, int):
            raise TypeError("nx must be an integer")
        if nx < 1:
            raise ValueError("nx must be a positive integer")

        if not isinstance(nodes, int):
            raise TypeError("nodes must be an integer")
        if nodes < 1:
            raise ValueError("nodes must be a positive integer")

        # Initialize weights and biases for the hidden layer
        self.W1 = np.random.randn(nodes, nx)  # Random weights for hidden layer
        self.b1 = np.zeros((nodes, 1))        # Zero bias for hidden layer
        self.A1 = 0                           # Placeholder for hidden layer activations

        # Initialize weights and biases for the output layer
        self.W2 = np.random.randn(1, nodes)  # Random weights for output layer
        self.b2 = 0                          # Zero bias for output layer
        self.A2 = 0                          # Placeholder for output layer activations
