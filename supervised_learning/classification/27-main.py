#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np

Deep = __import__('27-deep_neural_network').DeepNeuralNetwork
one_hot_encode = __import__('24-one_hot_encode').one_hot_encode
one_hot_decode = __import__('25-one_hot_decode').one_hot_decode

# Load data
lib = np.load('../data/MNIST.npz')
X_train_3D = lib['X_train']
Y_train = lib['Y_train']
X_valid_3D = lib['X_valid']
Y_valid = lib['Y_valid']

# Normalize data
X_train = X_train_3D.reshape((X_train_3D.shape[0], -1)).T / 255.0
X_valid = X_valid_3D.reshape((X_valid_3D.shape[0], -1)).T / 255.0

# One-hot encode labels
Y_train_one_hot = one_hot_encode(Y_train, 10)
Y_valid_one_hot = one_hot_encode(Y_valid, 10)

# Load or create the deep neural network
deep = Deep.load('27-saved.pkl')
if not deep:
    print("Creating a new deep neural network...")
    deep = Deep(X_train.shape[0], [128, 64, 10])
    deep.save('27-saved.pkl')

# Train the network
A_one_hot, cost = deep.train(X_train, Y_train_one_hot, iterations=100,
                             step=10, graph=True)
A = one_hot_decode(A_one_hot)
if A is None:
    raise ValueError("Error decoding output labels. Check one_hot_decode.")

# Calculate training accuracy
accuracy = np.sum(Y_train == A) / Y_train.shape[0] * 100
print("Train cost:", cost)
print("Train accuracy: {}%".format(accuracy))

# Evaluate the network
A_one_hot, cost = deep.evaluate(X_valid, Y_valid_one_hot)
A = one_hot_decode(A_one_hot)
if A is None:
    raise ValueError("Error decoding validation labels. Check one_hot_decode.")

# Calculate validation accuracy
accuracy = np.sum(Y_valid == A) / Y_valid.shape[0] * 100
print("Validation cost:", cost)
print("Validation accuracy: {}%".format(accuracy))

# Save the updated model
deep.save('27-output')

# Visualize predictions
fig = plt.figure(figsize=(10, 10))
for i in range(100):
    fig.add_subplot(10, 10, i + 1)
    plt.imshow(X_valid_3D[i])
    plt.title(A[i])
    plt.axis('off')
plt.tight_layout()
plt.show()
