#!/usr/bin/env python3
"""
Module for calculating the integral of a polynomial.
"""


def poly_integral(poly, C=0):
    """
    Calculates the integral of a polynomial represented as a list of coefficients.

    Args:
        poly (list): List of coefficients representing the polynomial.
        C (int, optional): Integration constant. Defaults to 0.

    Returns:
        list: List of coefficients representing the integral of the polynomial, or None if invalid.
    """
    if not isinstance(
        poly, list) or not all(
        isinstance(
            c, (int, float)) for c in poly) or not isinstance(
                C, (int, float)):
        return None

    integral = [C]  # Start with the integration constant
    for power, coefficient in enumerate(poly):
        integral.append(coefficient / (power + 1))

    return integral
