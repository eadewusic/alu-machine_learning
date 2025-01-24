#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np

Deep = __import__('23-deep_neural_network').DeepNeuralNetwork

lib_train = np.load('../data/Binary_Train.npz')
X_train_3D, Y_train = lib_train['X'], lib_train['Y']
X_train = X_train_3D.reshape((X_train_3D.shape[0], -1)).T

np.random.seed(1)
deep = Deep(X_train.shape[0], [5, 3, 1])
try:
    deep.train(X_train, Y_train, iterations=100, graph=False, step=105)
except ValueError as e:
    print(e)
try:
    deep.train(X_train, Y_train, graph=False, step=0)
except ValueError as e:
    print(e)
