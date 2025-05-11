#!/usr/bin/env python3
"""Create a class NST that performs tasks for Neural Style Transfer"""

import numpy as np
import tensorflow as tf


class NST:
    """Class that performs tasks for neural style transfer"""

    style_layers = ['block1_conv1', 'block2_conv1', 'block3_conv1',
                    'block4_conv1', 'block5_conv1']
    content_layer = 'block5_conv2'

    def __init__(self, style_image, content_image, alpha=1e4, beta=1):
        """
        Class constructor

        Parameters:
        - style_image: numpy.ndarray - the image used as a style reference
        - content_image: numpy.ndarray - the image used as a content reference
        - alpha: float - weight for content cost
        - beta: float - weight for style cost
        """
        if not isinstance(style_image, np.ndarray) or len(style_image.shape) != 3:
            raise TypeError("style_image must be a numpy.ndarray with shape (h, w, 3)")

        if not isinstance(content_image, np.ndarray) or len(content_image.shape) != 3:
            raise TypeError("content_image must be a numpy.ndarray with shape (h, w, 3)")

        if style_image.shape[2] != 3:
            raise TypeError("style_image must have 3 channels")
        if content_image.shape[2] != 3:
            raise TypeError("content_image must have 3 channels")

        if (not isinstance(alpha, (int, float))) or alpha < 0:
            raise TypeError("alpha must be a non-negative number")

        if (not isinstance(beta, (int, float))) or beta < 0:
            raise TypeError("beta must be a non-negative number")

        # TensorFlow 2.x enables eager execution by default

        # Set instance attributes
        self.style_image = self.scale_image(style_image)
        self.content_image = self.scale_image(content_image)
        self.alpha = alpha
        self.beta = beta

    @staticmethod
    def scale_image(image):
        """
        Rescales an image such that its pixel values are between 0 and 1
        and its largest side is 512 pixels while maintaining the aspect ratio.

        Parameters:
        - image: numpy.ndarray of shape (h, w, 3)

        Returns:
        - Tensor of shape (1, new_h, new_w, 3) with values in [0.0, 1.0]
        """
        if not isinstance(image, np.ndarray) or len(image.shape) != 3:
            raise TypeError("image must be a numpy.ndarray with shape (h, w, 3)")

        h, w, c = image.shape
        if h <= 0 or w <= 0 or c != 3:
            raise TypeError("image must be a numpy.ndarray with shape (h, w, 3)")

        if h > w:
            new_h = 512
            new_w = int(w * (512 / h))
        else:
            new_w = 512
            new_h = int(h * (512 / w))

        image = tf.convert_to_tensor(image, dtype=tf.float32)
        image = tf.image.resize(tf.expand_dims(image, axis=0),
                                size=(new_h, new_w),
                                method='bicubic')
        image /= 255.0
        image = tf.clip_by_value(image, 0.0, 1.0)
        return image
