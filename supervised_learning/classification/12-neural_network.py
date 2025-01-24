#!/usr/bin/env python3
"""
Defines a NeuralNetwork class that represents a neural network
with one hidden layer performing binary classification
"""

import numpy as np


class NeuralNetwork:
    """
    Class that represents a neural network with one
    hidden layer performing binary classification

    Constructor:
        def __init__(self, nx, nodes)

    Private instance attributes:
        __W1: the weights vector for the hidden layer
        __b1: the bias for the hidden layer
        __A1: the activated output for the hidden layer
        __W2: the weights vector for the output neuron
        __b2: the bias for the output neuron
        __A2: the activated output for the output neuron

    Public methods:
        def forward_prop(self, X): Calculates the forward
        propagation of the neural network
        def cost(self, Y, A): Calculates the cost using logistic regression
        def evaluate(self, X, Y): Evaluates the predictions
        of the neural network
    """

    def __init__(self, nx, nodes):
        """
        Initializes the neural network

        Arguments:
            nx [int]: The number of input features
            nodes [int]: The number of nodes in the hidden layer
        """
        if not isinstance(nx, int):
            raise TypeError("nx must be an integer")
        if nx < 1:
            raise ValueError("nx must be a positive integer")
        if not isinstance(nodes, int):
            raise TypeError("nodes must be an integer")
        if nodes < 1:
            raise ValueError("nodes must be a positive integer")

        self.__W1 = np.random.randn(nodes, nx)
        self.__b1 = np.zeros((nodes, 1))
        self.__A1 = 0
        self.__W2 = np.random.randn(1, nodes)
        self.__b2 = 0
        self.__A2 = 0

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
        """Getter for the weights of the output layer"""
        return self.__W2

    @property
    def b2(self):
        """Getter for the bias of the output layer"""
        return self.__b2

    @property
    def A2(self):
        """Getter for the activated output of the output layer"""
        return self.__A2

    def forward_prop(self, X):
        """
        Calculates forward propagation for the neural network

        Arguments:
            X [numpy.ndarray]: The input data

        Returns:
            tuple: The activated outputs of the hidden
            layer and the output layer
        """
        z1 = np.matmul(self.W1, X) + self.b1
        self.__A1 = 1 / (1 + np.exp(-z1))
        z2 = np.matmul(self.W2, self.__A1) + self.b2
        self.__A2 = 1 / (1 + np.exp(-z2))
        return self.A1, self.A2

    def cost(self, Y, A):
        """
        Calculates the cost of the neural network using logistic regression

        Arguments:
            Y [numpy.ndarray]: The correct labels
            A [numpy.ndarray]: The activated output of the
            neuron for each example

        Returns:
            float: The cost of the model
        """
        m = Y.shape[1]
        cost = -(1 / m) * np.sum(Y * np.log(A) +
                                 (1 - Y) * np.log(1.0000001 - A))
        return cost

    def evaluate(self, X, Y):
        """
        Evaluates the predictions of the neural network

        Arguments:
            X [numpy.ndarray]: The input data
            Y [numpy.ndarray]: The correct labels

        Returns:
            tuple: A tuple containing:
                - numpy.ndarray: The predictions with shape (1, m)
                - float: The cost of the network
        """
        A1, A2 = self.forward_prop(X)
        cost = self.cost(Y, A2)
        # Predicted labels: 1 if A2 >= 0.5 else 0
        predictions = np.where(A2 >= 0.5, 1, 0)
        return predictions, cost
