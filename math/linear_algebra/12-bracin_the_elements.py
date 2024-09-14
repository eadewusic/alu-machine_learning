#!/usr/bin/env python3
"""
Module for performing element-wise operations on numpy arrays
"""


def np_elementwise(mat1, mat2):
    """
    Performs element-wise addition, subtraction, multiplication, and division

    Args:
        mat1 (numpy.ndarray): The first input numpy array.
        mat2 (numpy.ndarray or scalar): The second input numpy array or scalar

    Returns:
        tuple: A tuple containing the element-wise sum, difference, product, and quotient
    """
    add = mat1 + mat2
    sub = mat1 - mat2
    mul = mat1 * mat2
    div = mat1 / mat2
    return add, sub, mul, div
