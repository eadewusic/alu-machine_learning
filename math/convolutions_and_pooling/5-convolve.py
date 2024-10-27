#!/usr/bin/env python3
"""
Defines a function that performs convolution on
images using multiple kernels
"""

import numpy as np


def convolve(images, kernels, padding='same', stride=(1, 1)):
    """
    Performs a convolution on images using multiple
    kernels with specified padding and stride

    Parameters:
        images (numpy.ndarray): Input images with shape (m, h, w, c)
            - m: number of images
            - h: height of images
            - w: width of images
            - c: number of channels in the images
        kernels (numpy.ndarray): Convolution kernels with
        shape (kh, kw, c, nc)
            - kh: kernel height
            - kw: kernel width
            - nc: number of kernels (output channels)
        padding (str or tuple): Padding method ('same', 'valid', or (ph, pw))
            - ph: padding for height if tuple
            - pw: padding for width if tuple
        stride (tuple): Stride for convolution (sh, sw)
            - sh: stride for height
            - sw: stride for width

    Returns:
        numpy.ndarray: Array containing the convolved
        images with multiple kernels
    """
    m, h, w, c = images.shape
    kh, kw, _, nc = kernels.shape
    sh, sw = stride

    # Determine padding
    if padding == 'same':
        ph = ((h - 1) * sh + kh - h) // 2 + 1
        pw = ((w - 1) * sw + kw - w) // 2 + 1
    elif padding == 'valid':
        ph, pw = 0, 0
    else:
        ph, pw = padding

    # Pad the images
    padded_images = np.pad(
        images, ((0, 0), (ph, ph), (pw, pw), (0, 0)),
        'constant', constant_values=0)

    # Output dimensions
    output_height = (h + 2 * ph - kh) // sh + 1
    output_width = (w + 2 * pw - kw) // sw + 1

    # Initialize output array
    convoluted = np.zeros((m, output_height, output_width, nc))

    # Perform convolution
    for i in range(output_height):
        for j in range(output_width):
            for n in range(nc):
                # Define region of interest for current position and kernel
                roi = padded_images[:, i * sh:i *
                                    sh + kh, j * sw:j * sw + kw, :]
                # Perform element-wise multiplication and sum over height,
                # width, and channels
                convoluted[:, i, j, n] = np.sum(
                    roi * kernels[:, :, :, n], axis=(1, 2, 3))

    return convoluted
