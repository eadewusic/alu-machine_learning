#!/usr/bin/env python3
"""
Defines a function that performs convolution on
images with channels
"""

import numpy as np


def convolve_channels(images, kernel, padding='same', stride=(1, 1)):
    """
    Performs a convolution on images with channels using
    specified padding and stride

    Parameters:
        images (numpy.ndarray): Input images with shape (m, h, w, c)
            - m: number of images
            - h: height of images
            - w: width of images
            - c: number of channels in the images
        kernel (numpy.ndarray): Convolution kernel with shape (kh, kw, c)
            - kh: kernel height
            - kw: kernel width
            - c: number of channels (should match the channels in images)
        padding (str or tuple): Padding method ('same', 'valid', or (ph, pw))
            - ph: padding for height if tuple
            - pw: padding for width if tuple
        stride (tuple): Stride for convolution (sh, sw)
            - sh: stride for height
            - sw: stride for width

    Returns:
        numpy.ndarray: Array containing the convolved images
    """
    m, h, w, c = images.shape
    kh, kw, _ = kernel.shape
    sh, sw = stride

    # Determine padding
    if padding == 'same':
        ph = (((h - 1) * sh + kh - h) // 2) + 1
        pw = (((w - 1) * sw + kw - w) // 2) + 1
    elif padding == 'valid':
        ph, pw = 0, 0
    else:
        ph, pw = padding

    # Pad the images with zero padding based on ph and pw
    padded_images = np.pad(
        images, ((0, 0), (ph, ph), (pw, pw), (0, 0)), 'constant', constant_values=0)

    # Calculate output dimensions
    output_height = (h + 2 * ph - kh) // sh + 1
    output_width = (w + 2 * pw - kw) // sw + 1

    # Initialize output array for the convolved images
    convoluted = np.zeros((m, output_height, output_width))

    # Perform convolution with stride
    i = 0
    for x in range(0, h + 2 * ph - kh + 1, sh):
        j = 0
        for y in range(0, w + 2 * pw - kw + 1, sw):
            # Element-wise multiplication and sum across the
            # height, width, and channels
            output = np.sum(
                padded_images[:, x:x + kh, y:y + kw, :] * kernel, axis=(1, 2, 3))
            convoluted[:, i, j] = output
            j += 1
        i += 1

    return convoluted
