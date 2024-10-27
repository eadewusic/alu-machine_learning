#!/usr/bin/env python3
"""
Module for performing same convolution on grayscale images.
"""

import numpy as np

def convolve_grayscale_same(images, kernel):
    """
    Performs a same convolution on grayscale images with padding.

    Parameters:
        images (numpy.ndarray): Input images with shape (m, h, w)
            - m: number of images
            - h: height in pixels of the images
            - w: width in pixels of the images
        kernel (numpy.ndarray): Convolution kernel with shape (kh, kw)
            - kh: height of the kernel
            - kw: width of the kernel

    Returns:
        numpy.ndarray: Array of convolved images with the same dimensions as the input images.
    """
    m, height, width = images.shape
    kh, kw = kernel.shape

    # Calculate padding for height and width
    pad_h = (kh - 1) // 2
    pad_w = (kw - 1) // 2

    # Pad images with zero padding on all sides
    padded_images = np.pad(images, ((0, 0), (pad_h, pad_h), (pad_w, pad_w)), mode='constant', constant_values=0)

    # Initialize the output array with the same dimensions as input images
    convoluted = np.zeros((m, height, width))

    # Perform the convolution using two for loops
    for h in range(height):
        for w in range(width):
            # Apply kernel on the current slice
            output = np.sum(padded_images[:, h: h + kh, w: w + kw] * kernel, axis=(1, 2))
            convoluted[:, h, w] = output

    return convoluted
