#!/usr/bin/env python3
import numpy as np

def convolve_grayscale_valid(images, kernel):
    """Perform valid convolution on grayscale images.

    Args:
        images (np.ndarray): Input images of shape (m, h, w).
        kernel (np.ndarray): Convolution kernel of shape (kh, kw).

    Returns:
        np.ndarray: Convolved images.
    """
    m, h, w = images.shape  # Get the shape of the input images
    kh, kw = kernel.shape    # Get the shape of the kernel

    # Calculate the dimensions of the output images
    output_h = h - kh + 1
    output_w = w - kw + 1

    # Initialize the output array
    convolved_images = np.zeros((m, output_h, output_w))

    # Perform the convolution
    for i in range(m):  # Loop over each image
        for y in range(output_h):  # Loop over height of the output
            for x in range(output_w):  # Loop over width of the output
                # Apply the kernel to the current region of the image
                convolved_images[i, y, x] = np.sum(
                    images[i, y:y + kh, x:x + kw] * kernel
                )

    return convolved_images
