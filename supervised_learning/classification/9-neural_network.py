#!/usr/bin/env python3
"""
Defines the NeuralNetwork class that represents a neural network
with one hidden layer performing binary classification
"""

import numpy as np


class NeuralNetwork:
    """
    A class representing a neural network with one hidden layer
    performing binary classification
    """

    def __init__(self, nx, nodes):
        """
        Class constructor

        Parameters:
        nx (int): The number of input features
        nodes (int): The number of nodes in the hidden layer

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

        # Private instance attributes
        self.__W1 = np.random.randn(nodes, nx)
        self.__b1 = np.zeros((nodes, 1))
        self.__A1 = 0
        self.__W2 = np.random.randn(1, nodes)
        self.__b2 = 0
        self.__A2 = 0

    # Getters for the private attributes
    @property
    def W1(self):
        """Getter for the weights of the hidden layer"""
        return self.__W1

    @property
    def b1(self):
        """Getter for the bias of the hidden layer"""
        return self.__b1

    @property
    def A1(self):
        """Getter for the activated output of the hidden layer"""
        return self.__A1

    @property
    def W2(self):
        """Getter for the weights of the output neuron"""
        return self.__W2

    @property
    def b2(self):
        """Getter for the bias of the output neuron"""
        return self.__b2

    @property
    def A2(self):
        """Getter for the activated output of the output neuron"""
        return self.__A2
