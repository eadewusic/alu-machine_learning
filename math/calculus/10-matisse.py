#!/usr/bin/env python3
"""
Module for calculating the derivative of a polynomial.
"""


def poly_derivative(poly):
    """Calculates the derivative of a polynomial."""
    if not isinstance(
        poly, list) or any(
        not isinstance(
            coef, (int, float)) for coef in poly):
        return None

    # Calculate derivative coefficients
    derivative = [(i * coef) for i, coef in enumerate(poly) if i > 0]

    if not derivative:
        return [0]  # If the derivative is 0, return [0]

    return derivative
