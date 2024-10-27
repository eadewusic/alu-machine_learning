#!/usr/bin/env python3
"""
Defines a function that performs convolution on
grayscale images with options for padding and stride
"""

import numpy as np


def convolve_grayscale(images, kernel, padding='same', stride=(1, 1)):
    """
    Performs a convolution on grayscale images with
    specified padding and stride

    Parameters:
        images (numpy.ndarray): Input images with shape (m, h, w)
            - m: number of images
            - h: height of images
            - w: width of images
        kernel (numpy.ndarray): Convolution kernel with shape (kh, kw)
            - kh: kernel height
            - kw: kernel width
        padding (str or tuple): Padding method ('same', 'valid', or (ph, pw))
            - ph: padding for height if tuple
            - pw: padding for width if tuple
        stride (tuple): Stride for convolution (sh, sw)
            - sh: stride for height
            - sw: stride for width

    Returns:
        numpy.ndarray: Array containing the convolved images
    """
    m, height, width = images.shape
    kh, kw = kernel.shape
    sh, sw = stride

    # Determine padding
    if padding == 'same':
        ph = (kh - 1) // 2
        pw = (kw - 1) // 2
    elif padding == 'valid':
        ph, pw = 0, 0
    elif isinstance(padding, tuple):
        ph, pw = padding
    else:
        raise ValueError("Padding must be 'same', 'valid', or a tuple")

    # Pad the images
    padded_images = np.pad(
        images, ((0, 0), (ph, ph), (pw, pw)), 'constant', constant_values=0)

    # Calculate output dimensions
    new_height = (height + 2 * ph - kh) // sh + 1
    new_width = (width + 2 * pw - kw) // sw + 1

    # Initialize the output array
    convoluted = np.zeros((m, new_height, new_width))

    # Perform convolution with stride
    for i in range(new_height):
        for j in range(new_width):
            # Compute the convolution over the current region
            h_start = i * sh
            h_end = h_start + kh
            w_start = j * sw
            w_end = w_start + kw
            output = np.sum(
                padded_images[:, h_start:h_end, w_start:w_end] * kernel, axis=(1, 2))
            convoluted[:, i, j] = output

    return convoluted
