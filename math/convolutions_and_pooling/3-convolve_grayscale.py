#!/usr/bin/env python3
"""
Defines a function that performs convolution on
grayscale images with specified padding and stride
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
        ph = (((height - 1) * sh + kh - height) // 2) + 1
        pw = (((width - 1) * sw + kw - width) // 2) + 1
    elif padding == 'valid':
        ph, pw = 0, 0
    else:
        ph, pw = padding

    # Pad the images with zero padding based on ph and pw
    padded_images = np.pad(
        images, ((0, 0), (ph, ph), (pw, pw)), 'constant', constant_values=0)

    # Calculate output dimensions
    output_height = (height + 2 * ph - kh) // sh + 1
    output_width = (width + 2 * pw - kw) // sw + 1

    # Initialize output array for the convolved images
    convoluted = np.zeros((m, output_height, output_width))

    # Perform convolution with stride
    i = 0
    for h in range(0, height + 2 * ph - kh + 1, sh):
        j = 0
        for w in range(0, width + 2 * pw - kw + 1, sw):
            output = np.sum(
                padded_images[:, h:h + kh, w:w + kw] * kernel, axis=(1, 2))
            convoluted[:, i, j] = output
            j += 1
        i += 1

    return convoluted
