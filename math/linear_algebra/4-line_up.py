#!/usr/bin/env python3

"""
4-line_up - Module for element-wise addition of two arrays.

This module contains the add_arrays function which adds two arrays element-wise.
"""


def add_arrays(arr1, arr2):
    """
    Add two arrays element-wise.

    Args:
        arr1 (list): The first list of integers or floats.
        arr2 (list): The second list of integers or floats.

    Returns:
        list or None: A new list containing the element-wise sum of arr1 and arr2,
                      or None if arr1 and arr2 are not the same shape.
    """
    if len(arr1) != len(arr2):
        return None
    return [x + y for x, y in zip(arr1, arr2)]
