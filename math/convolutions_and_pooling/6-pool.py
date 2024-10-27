#!/usr/bin/env python3
"""
Defines a function that performs pooling on images
"""

import numpy as np


def pool(images, kernel_shape, stride, mode='max'):
    """
    Performs pooling on images with a specified kernel
    shape, stride, and mode

    Parameters:
        images (numpy.ndarray): Input images with shape (m, h, w, c)
            - m: number of images
            - h: height of images
            - w: width of images
            - c: number of channels in the images
        kernel_shape (tuple): Shape of the pooling kernel (kh, kw)
            - kh: kernel height
            - kw: kernel width
        stride (tuple): Stride for pooling (sh, sw)
            - sh: stride for height
            - sw: stride for width
        mode (str): Pooling mode ('max' or 'avg')

    Returns:
        numpy.ndarray: Array containing the pooled images
    """
    m, h, w, c = images.shape
    kh, kw = kernel_shape
    sh, sw = stride

    # Calculate output dimensions
    output_height = (h - kh) // sh + 1
    output_width = (w - kw) // sw + 1

    # Initialize output array
    pooled = np.zeros((m, output_height, output_width, c))

    # Perform pooling
    for i in range(output_height):
        for j in range(output_width):
            # Define the region of interest for current position
            roi = images[:, i * sh:i * sh + kh, j * sw:j * sw + kw, :]
            # Apply the appropriate pooling operation
            if mode == 'max':
                pooled[:, i, j, :] = np.max(roi, axis=(1, 2))
            elif mode == 'avg':
                pooled[:, i, j, :] = np.mean(roi, axis=(1, 2))

    return pooled
