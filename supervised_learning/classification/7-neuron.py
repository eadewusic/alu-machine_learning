#!/usr/bin/env python3
"""
This module defines the Neuron class, which represents a single neuron
performing binary classification. It includes methods for forward propagation,
cost calculation, evaluation, gradient descent, and training
"""

import numpy as np
import matplotlib.pyplot as plt


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
            Y (numpy.ndarray): Correct labels for the input data
            A (numpy.ndarray): Activated output of the neuron

        Returns:
            float: The cost of the model
        """
        m = Y.shape[1]
        cost = -(1 / m) * np.sum(Y * np.log(A) + (1 - Y) * np.log(1.0000001 - A))
        return cost

    def evaluate(self, X, Y):
        """
        Evaluates the neuron's predictions

        Args:
            X (numpy.ndarray): Input data
            Y (numpy.ndarray): Correct labels

        Returns:
            tuple: Predictions and cost of the model
        """
        A = self.forward_prop(X)
        cost = self.cost(Y, A)
        predictions = np.where(A >= 0.5, 1, 0)
        return predictions, cost

    def gradient_descent(self, X, Y, A, alpha=0.05):
        """
        Performs one pass of gradient descent to update the weights and bias

        Args:
            X (numpy.ndarray): Input data
            Y (numpy.ndarray): Correct labels
            A (numpy.ndarray): Activated output
            alpha (float): Learning rate
        """
        m = X.shape[1]
        dZ = A - Y
        dW = (1 / m) * np.dot(dZ, X.T)
        db = (1 / m) * np.sum(dZ)

        self.__W -= alpha * dW
        self.__b -= alpha * db

    def train(self, X, Y, iterations=5000, alpha=0.05, verbose=True, graph=True, step=100):
        """
        Trains the neuron using gradient descent.

        Args:
            X (numpy.ndarray): Input data
            Y (numpy.ndarray): Correct labels
            iterations (int): Number of iterations to train over
            alpha (float): Learning rate
            verbose (bool): Whether to print cost information
            graph (bool): Whether to graph the training cost
            step (int): Interval for verbose and graph updates

        Returns:
            tuple: Evaluation of the training data after training

        Raises:
            TypeError: If iterations is not an integer
            ValueError: If iterations is not positive
            TypeError: If alpha is not a float
            ValueError: If alpha is not positive
            TypeError: If step is not an integer
            ValueError: If step is not positive and <= iterations
        """
        if not isinstance(iterations, int):
            raise TypeError("iterations must be an integer")
        if iterations <= 0:
            raise ValueError("iterations must be a positive integer")
        if not isinstance(alpha, float):
            raise TypeError("alpha must be a float")
        if alpha <= 0:
            raise ValueError("alpha must be positive")
        if (verbose or graph) and not isinstance(step, int):
            raise TypeError("step must be an integer")
        if (verbose or graph) and (step <= 0 or step > iterations):
            raise ValueError("step must be positive and <= iterations")

        costs = []
        for i in range(iterations + 1):
            A = self.forward_prop(X)
            self.gradient_descent(X, Y, A, alpha)

            if i % step == 0 or i == iterations:
                cost = self.cost(Y, A)
                costs.append((i, cost))
                if verbose:
                    print(f"Cost after {i} iterations: {cost}")

        if graph:
            iterations, cost_values = zip(*costs)
            plt.plot(iterations, cost_values, 'b-')
            plt.xlabel("iteration")
            plt.ylabel("cost")
            plt.title("Training Cost")
            plt.show()

        return self.evaluate(X, Y)
