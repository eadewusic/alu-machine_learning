#!/usr/bin/env python3
"""Module for deep neural network class"""
import numpy as np
import matplotlib.pyplot as plt
import pickle


class DeepNeuralNetwork:
    """Defines a deep neural network for binary classification"""

    def __init__(self, nx, layers):
        if not isinstance(nx, int):
            raise TypeError("nx must be an integer")
        if nx < 1:
            raise ValueError("nx must be a positive integer")
        if not isinstance(layers, list) or len(layers) == 0:
            raise TypeError("layers must be a list of positive integers")
        if any(not isinstance(x, int) or x <= 0 for x in layers):
            raise TypeError("layers must be a list of positive integers")

        self.__nx = nx
        self.__layers = layers
        self.__L = len(layers)
        self.__cache = {}
        self.__weights = {}

        for i, nodes in enumerate(layers):
            w_key = "W{}".format(i + 1)
            b_key = "b{}".format(i + 1)
            self.__weights[b_key] = np.zeros((nodes, 1))
            if i == 0:
                self.__weights[w_key] = np.random.randn(nodes, nx) * np.sqrt(2 / nx)
            else:
                self.__weights[w_key] = np.random.randn(nodes, layers[i - 1]) * np.sqrt(2 / layers[i - 1])

    @property
    def L(self):
        return self.__L

    @property
    def cache(self):
        return self.__cache

    @property
    def weights(self):
        return self.__weights

    def sigmoid(self, z):
        return 1 / (1 + np.exp(-z))

    def softmax(self, z):
        z_exp = np.exp(z - np.max(z, axis=0, keepdims=True))
        return z_exp / np.sum(z_exp, axis=0, keepdims=True)

    def forward_prop(self, X):
        self.__cache["A0"] = X
        for i in range(self.__L):
            w_key = "W{}".format(i + 1)
            b_key = "b{}".format(i + 1)
            a_prev = self.__cache[f"A{i}"]
            z = np.matmul(self.__weights[w_key], a_prev) + self.__weights[b_key]
            self.__cache[f"A{i + 1}"] = self.sigmoid(z) if i < self.__L - 1 else self.softmax(z)
        return self.__cache[f"A{self.__L}"], self.__cache

    def cost(self, Y, A):
        m = Y.shape[1]
        cost = -np.sum(Y * np.log(A)) / m
        return cost

    def evaluate(self, X, Y):
        A, _ = self.forward_prop(X)
        cost = self.cost(Y, A)
        predictions = np.where(A == np.max(A, axis=0, keepdims=True), 1, 0)
        return predictions, cost

    def gradient_descent(self, Y, cache, alpha=0.05):
        m = Y.shape[1]
        dAl = cache[f"A{self.__L}"] - Y
        for i in reversed(range(1, self.__L + 1)):
            a_prev = cache[f"A{i - 1}"]
            w_key, b_key = f"W{i}", f"b{i}"
            dW = np.matmul(dAl, a_prev.T) / m
            db = np.sum(dAl, axis=1, keepdims=True) / m
            dAl = np.matmul(self.__weights[w_key].T, dAl) * (a_prev * (1 - a_prev))
            self.__weights[w_key] -= alpha * dW
            self.__weights[b_key] -= alpha * db

    def train(self, X, Y, iterations=5000, alpha=0.05, verbose=True, graph=True, step=100):
        if not isinstance(iterations, int) or iterations <= 0:
            raise ValueError("iterations must be a positive integer")
        if not isinstance(alpha, float) or alpha <= 0:
            raise ValueError("alpha must be positive")
        if verbose or graph:
            if not isinstance(step, int) or step <= 0 or step > iterations:
                raise ValueError("step must be positive and <= iterations")

        costs, steps = [], []
        for i in range(iterations):
            A, _ = self.forward_prop(X)
            self.gradient_descent(Y, self.__cache, alpha)
            if i % step == 0 or i == iterations - 1:
                cost = self.cost(Y, A)
                costs.append(cost)
                steps.append(i)
                if verbose:
                    print(f"Cost after {i} iterations: {cost:.4f}")

        if graph:
            plt.plot(steps, costs)
            plt.xlabel("Iterations")
            plt.ylabel("Cost")
            plt.title("Training Cost")
            plt.show()

        return self.evaluate(X, Y)

    def save(self, filename):
        if not filename.endswith(".pkl"):
            filename += ".pkl"
        with open(filename, "wb") as f:
            pickle.dump(self, f)

    @staticmethod
    def load(filename):
        try:
            with open(filename, "rb") as f:
                return pickle.load(f)
        except FileNotFoundError:
            return None
