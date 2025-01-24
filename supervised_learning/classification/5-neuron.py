#!/usr/bin/env python3
"""
This module defines the Neuron class, which represents a single neuron
performing binary classification. It includes methods for forward propagation,
cost calculation, evaluation, and gradient descent
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
        Z = np.dot(self.__W, X) + self.__b
        self.__A = 1 / (1 + np.exp(-Z))
        return self.__A

    def cost(self, Y, A):
        """
        Calculates the cost of the model using logistic regression

        Args:
            Y (numpy.ndarray): Correct labels for the
            input data with shape (1, m)
            A (numpy.ndarray): Activated output of the neuron with shape (1, m)

        Returns:
            float: The cost of the model
        """
        m = Y.shape[1]
        cost = -(1 / m) * np.sum(Y * np.log(A) +
                                 (1 - Y) * np.log(1.0000001 - A))
        return cost

    def evaluate(self, X, Y):
        """
        Evaluates the neuron's predictions

        Args:
            X (numpy.ndarray): Input data with shape (nx, m)
            Y (numpy.ndarray): Correct labels for
            the input data with shape (1, m)

        Returns:
            tuple: A tuple containing:
                - numpy.ndarray: Predictions with shape (1, m)
                - float: Cost of the network
        """
        A = self.forward_prop(X)  # Perform forward propagation
        cost = self.cost(Y, A)   # Calculate the cost
        # Generate predictions: 1 if A >= 0.5, else 0
        predictions = np.where(A >= 0.5, 1, 0)
        return predictions, cost

    def gradient_descent(self, X, Y, A, alpha=0.05):
        """
        Performs one pass of gradient descent to update the weights and bias

        Args:
            X (numpy.ndarray): Input data with shape (nx, m)
            Y (numpy.ndarray): Correct labels with shape (1, m)
            A (numpy.ndarray): Activated output with shape (1, m)
            alpha (float): Learning rate
        """
        m = X.shape[1]  # Number of examples
        dZ = A - Y      # Derivative of cost with respect to Z
        dW = (1 / m) * np.dot(dZ, X.T)  # Gradient of weights
        db = (1 / m) * np.sum(dZ)       # Gradient of bias

        # Update weights and bias
        self.__W -= alpha * dW
        self.__b -= alpha * db
