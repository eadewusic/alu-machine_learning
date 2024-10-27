#!/usr/bin/env python3
"""
Defines a function that performs convolution with
custom padding on grayscale images
"""

import numpy as np


def convolve_grayscale_padding(images, kernel, padding):
    """
    Performs a convolution on grayscale images with custom padding

    Parameters:
        images (numpy.ndarray): Input images with shape (m, h, w)
            - m: number of images
            - h: height in pixels of the images
            - w: width in pixels of the images
        kernel (numpy.ndarray): Convolution kernel with shape (kh, kw)
            - kh: height of the kernel
            - kw: width of the kernel
        padding (tuple): Tuple of (ph, pw)
            - ph: padding for height
            - pw: padding for width

    Returns:
        numpy.ndarray: Array of convolved images with
        dimensions adjusted by the padding
    """
    m, height, width = images.shape
    kh, kw = kernel.shape
    ph, pw = padding

    # Apply custom padding to images with zero padding on all sides
    padded_images = np.pad(
        images, ((0, 0), (ph, ph), (pw, pw)), 'constant', constant_values=0)

    # Calculate the dimensions of the output
    new_height = height + 2 * ph - kh + 1
    new_width = width + 2 * pw - kw + 1

    # Initialize the output array
    convoluted = np.zeros((m, new_height, new_width))

    # Perform the convolution using two for loops
    for h in range(new_height):
        for w in range(new_width):
            # Apply kernel on the current slice
            output = np.sum(
                padded_images[:, h: h + kh, w: w + kw] * kernel, axis=(1, 2))
            convoluted[:, h, w] = output

    return convoluted
