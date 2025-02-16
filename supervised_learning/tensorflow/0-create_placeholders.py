#!/usr/bin/env python3
"""
This module defines a function that creates placeholders for the input data
and one-hot encoded labels in a neural network.

The placeholders are used for feeding data into the model during training.

Functions:
    create_placeholders(nx, classes): Creates placeholders for input data and labels.
"""

import tensorflow as tf


def create_placeholders(nx, classes):
    """Creates placeholders for input data and labels"""
    x = tf.placeholder(tf.float32, shape=(None, nx), name="x")
    y = tf.placeholder(tf.float32, shape=(None, classes), name="y")
    return x, y


# Example usage
if __name__ == "__main__":
    x, y = create_placeholders(784, 10)
    print(x)
    print(y)
