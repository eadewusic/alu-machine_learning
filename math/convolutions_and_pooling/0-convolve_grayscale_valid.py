#!/usr/bin/env python3
import numpy as np

"""
Module for performing valid convolution on grayscale images.
"""

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
                # Extract the region from the image
                region = images[i, y:y + kh, x:x + kw]  # Current region
                convolved_value = np.sum(region * kernel)  # Convolution operation
                convolved_images[i, y, x] = convolved_value

                # Debugging output
                if i == 0:  # Only print for the first image
                    print(f"Image: {i}, Position: ({y}, {x}), Region: {region}, "
                          f"Kernel: {kernel}, Convolved Value: {convolved_value}")

    return convolved_images
