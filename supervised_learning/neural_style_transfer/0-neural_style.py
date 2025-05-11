#!/usr/bin/env python3
"""
Neural Style Transfer Initialization
"""

import numpy as np
import tensorflow as tf


class NST:
    """
    NST class for performing Neural Style Transfer
    """

    style_layers = [
        'block1_conv1',
        'block2_conv1',
        'block3_conv1',
        'block4_conv1',
        'block5_conv1'
    ]
    content_layer = 'block5_conv2'

    def __init__(self, style_image, content_image, alpha=1e4, beta=1):
        """
        Class constructor for NST

        Args:
        - style_image: numpy.ndarray of shape (h, w, 3)
        - content_image: numpy.ndarray of shape (h, w, 3)
        - alpha: weight for content cost
        - beta: weight for style cost
        """

        # Type and shape validation
        if not isinstance(style_image, np.ndarray) or style_image.ndim != 3 or style_image.shape[2] != 3:
            raise TypeError("style_image must be a numpy.ndarray with shape (h, w, 3)")

        if not isinstance(content_image, np.ndarray) or content_image.ndim != 3 or content_image.shape[2] != 3:
            raise TypeError("content_image must be a numpy.ndarray with shape (h, w, 3)")

        if not isinstance(alpha, (int, float)) or alpha < 0:
            raise TypeError("alpha must be a non-negative number")

        if not isinstance(beta, (int, float)) or beta < 0:
            raise TypeError("beta must be a non-negative number")

        # Enable eager execution for TF1.x compatibility
        if tf.__version__.startswith('1.'):
            tf.enable_eager_execution()

        # Set instance attributes
        self.style_image = self.scale_image(style_image)
        self.content_image = self.scale_image(content_image)
        self.alpha = alpha
        self.beta = beta

    @staticmethod
    def scale_image(image):
        """
        Rescales an image such that its largest side is 512 pixels
        and pixel values are normalized to range [0, 1]

        Returns: Scaled image as tf.Tensor with shape (1, h_new, w_new, 3)
        """
        if not isinstance(image, np.ndarray) or image.ndim != 3 or image.shape[2] != 3:
            raise TypeError("image must be a numpy.ndarray with shape (h, w, 3)")

        h, w, _ = image.shape

        if h > w:
            new_h = 512
            new_w = int((w / h) * 512)
        else:
            new_w = 512
            new_h = int((h / w) * 512)

        image = tf.convert_to_tensor(image, dtype=tf.float32)
        image = tf.image.resize(image, (new_h, new_w), method='bicubic')
        image /= 255.0
        image = tf.expand_dims(image, axis=0)

        return tf.clip_by_value(image, 0.0, 1.0)
