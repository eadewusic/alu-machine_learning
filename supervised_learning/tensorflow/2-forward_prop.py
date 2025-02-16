#!/usr/bin/env python3
"""
This module defines the function for forward propagation in
a neural network

The function constructs the forward propagation graph by iterating
through the layers specified in the `layer_sizes` list, applying
the corresponding activation function from the `activations` list

Functions:
    forward_prop(x, layer_sizes=[], activations=[]): Builds the forward
    propagation graph and returns the output tensor of the network
"""

import tensorflow as tf

# Importing the create_layer function
create_layer = __import__('1-create_layer').create_layer


def forward_prop(x, layer_sizes=[], activations=[]):
    """
    Creates the forward propagation graph for a neural network

    Args:
    x (tensor): The placeholder for the input data
    layer_sizes (list): A list containing the number of nodes
    in each layer
    activations (list): A list containing the activation functions
    for each layer

    Returns:
    tensor: The prediction tensor of the neural network after
    forward propagation
    """
    # Initialize the input tensor as the first layer
    prev = x

    # Loop through the layers and create them
    for i in range(len(layer_sizes)):
        prev = create_layer(prev, layer_sizes[i], activations[i])

    # Add softmax activation to the final layer if it's for classification
    return tf.nn.softmax(prev)
