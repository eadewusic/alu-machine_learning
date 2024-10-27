#!/usr/bin/env python3
"""
Module for performing valid convolution on grayscale images.
"""

import numpy as np

def convolve_grayscale_valid(images, kernel):
    """
    Performs a valid convolution on grayscale images.

    Parameters:
        images (numpy.ndarray): Input images with shape (m, h, w)
            - m: number of images
            - h: height in pixels of all images
            - w: width in pixels of all images
        kernel (numpy.ndarray): Convolution kernel with shape (kh, kw)
            - kh: height of the kernel
            - kw: width of the kernel

    The function may only use two for loops maximum and no other loops are allowed.

    Returns:
        numpy.ndarray: Array of convolved images.
    """
    # Extract dimensions
    m, height, width = images.shape
    kh, kw = kernel.shape

    # Initialize the output array with the correct dimensions
    convoluted = np.zeros((m, height - kh + 1, width - kw + 1))

    # Perform the convolution using two for loops
    for h in range(height - kh + 1):
        for w in range(width - kw + 1):
            # Perform element-wise multiplication and summation over the current slice
            output = np.sum(images[:, h: h + kh, w: w + kw] * kernel, axis=(1, 2))
            convoluted[:, h, w] = output

    return convoluted
