#!/usr/bin/env python3
"""Neural Style Transfer"""
import numpy as np
import tensorflow as tf
from tensorflow.keras.applications.vgg19 import VGG19, preprocess_input
from tensorflow.keras.models import Model


class NST:
    """Neural Style Transfer class"""

    style_layers = ['block1_conv1',
                    'block2_conv1',
                    'block3_conv1',
                    'block4_conv1',
                    'block5_conv1']
    content_layer = 'block5_conv2'

    def __init__(self, style_image, content_image, alpha=1e4, beta=1):
        """Initialize NST instance and validate inputs"""
        if not isinstance(style_image, np.ndarray) or style_image.ndim != 3 or style_image.shape[2] != 3:
            raise TypeError("style_image must be a numpy.ndarray with shape (h, w, 3)")
        if not isinstance(content_image, np.ndarray) or content_image.ndim != 3 or content_image.shape[2] != 3:
            raise TypeError("content_image must be a numpy.ndarray with shape (h, w, 3)")
        if not isinstance(alpha, (int, float)) or alpha < 0:
            raise TypeError("alpha must be a non-negative number")
        if not isinstance(beta, (int, float)) or beta < 0:
            raise TypeError("beta must be a non-negative number")

        tf.config.run_functions_eagerly(True)

        self.alpha = alpha
        self.beta = beta
        self.style_image = self.scale_image(style_image)
        self.content_image = self.scale_image(content_image)
        self.model = self.load_model()

    @staticmethod
    def scale_image(image):
        """Rescales an image to max 512 px, keeps aspect ratio, and normalizes"""
        if not isinstance(image, np.ndarray) or image.ndim != 3 or image.shape[2] != 3:
            raise TypeError("image must be a numpy.ndarray with shape (h, w, 3)")

        h, w, _ = image.shape
        if h > w:
            new_h = 512
            new_w = int(w * (512 / h))
        else:
            new_w = 512
            new_h = int(h * (512 / w))

        image = tf.convert_to_tensor(image, dtype=tf.float32)
        image = tf.image.resize(image, (new_h, new_w), method='bicubic')
        image = tf.clip_by_value(image / 255.0, 0.0, 1.0)
        image = tf.expand_dims(image, axis=0)

        return image

    def load_model(self):
        """Loads VGG19 model for style/content cost computation"""
        vgg = VGG19(include_top=False, weights='imagenet')
        vgg.trainable = False

        outputs = [vgg.get_layer(name).output for name in self.style_layers + [self.content_layer]]
        model = Model(inputs=vgg.input, outputs=outputs)
        model.trainable = False

        return model
