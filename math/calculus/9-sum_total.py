#!/usr/bin/env python3
"""
Module for calculating the sum of squares of the first n integers.
"""

def summation_i_squared(n):
    """Calculates the sum of squares of the first n integers."""
    if not isinstance(n, int) or n < 1:
        return None
    return (n * (n + 1) * (2 * n + 1)) // 6
