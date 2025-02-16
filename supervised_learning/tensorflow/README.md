# TensorFlow

## Overview
This project focuses on mastering the fundamental concepts of TensorFlow 1.12, including computational graphs, tensors, sessions, operations, and neural network training. The objective is to build a strong understanding of how TensorFlow works at a low level, including model saving/loading, using variables, constants, placeholders, and more.

## Learning Objectives
By the end of this project, you should be able to:
- Explain what TensorFlow is and how it works.
- Understand and use computational graphs and sessions.
- Work with tensors, variables, constants, and placeholders.
- Perform operations and use namespaces.
- Train a neural network in TensorFlow 1.12.
- Save and restore models using checkpoints.
- Utilize the graph collection for storing and retrieving variables.

## Requirements
- **Operating System**: Ubuntu 16.04 LTS
- **Python Version**: 3.5
- **TensorFlow Version**: 1.12
- **NumPy Version**: 1.15
- All scripts must be executable and follow the `pycodestyle` style (version 2.4).
- All modules, classes, and functions must be properly documented.
- Only `import tensorflow as tf` is allowed (no `keras` usage).

## Example: Basic TensorFlow Graph
```python
#!/usr/bin/env python3
import tensorflow as tf

# Define a computation graph
a = tf.constant(5, name="a")
b = tf.constant(3, name="b")
sum_ab = tf.add(a, b, name="sum")

# Create a session and run the graph
with tf.Session() as sess:
    result = sess.run(sum_ab)
    print("Sum:", result)  # Output: 8
```

## Model Saving and Loading Example
```python
# Saving a model
saver = tf.train.Saver()
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    saver.save(sess, "model.ckpt")
```

```python
# Loading a model
saver = tf.train.Saver()
with tf.Session() as sess:
    saver.restore(sess, "model.ckpt")
```
