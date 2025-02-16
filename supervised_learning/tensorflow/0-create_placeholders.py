#!/usr/bin/env python3
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
