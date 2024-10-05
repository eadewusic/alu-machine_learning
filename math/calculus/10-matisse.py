#!/usr/bin/env python3
"""
Module for calculating the derivative of a polynomial.
"""


def poly_derivative(poly):
    """Calculates the derivative of a polynomial."""
    # Check if poly is a list and contains only integers or floats
    if not isinstance(
        poly, list) or any(
        not isinstance(
            coef, (int, float)) for coef in poly):
        return None

    # Calculate derivative coefficients
    derivative = [(i * coef) for i, coef in enumerate(poly) if i > 0]

    # If the derivative list is empty, it means the polynomial was constant
    if not derivative:
        return [0]

    return derivative
