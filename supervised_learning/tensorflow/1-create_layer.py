#!/usr/bin/env python3
"""
This module defines a function to create a layer in a neural network

The function creates a new layer by initializing weights using He
initialization (variance scaling), adding biases, and applying the
specified activation function. The layer is named "layer" for distinction

Functions:
    create_layer(prev, n, activation): Creates a new layer with the
    specified number of nodes and activation function
"""

import tensorflow as tf


def create_layer(prev, n, activation):
    """
    Creates a layer for the neural network

    Args:
    prev (tensor): The output tensor of the previous layer
    n (int): The number of nodes in the current layer
    activation (function): The activation function to apply to the layer

    Returns:
    tensor: The output tensor of the current layer
    """
    # Initialize the weights using He initialization
    weights = tf.Variable(
        tf.contrib.layers.variance_scaling_initializer(
            mode="FAN_AVG")(
            shape=[
                prev.shape[1].value,
                n]),
        name='weights')

    # Initialize biases as zeros
    biases = tf.Variable(tf.zeros([n]), name='biases')

    # Linear transformation (W * X + b)
    z = tf.add(tf.matmul(prev, weights), biases, name="z")

    # Apply the activation function
    layer = activation(z, name="activation")

    return layer
