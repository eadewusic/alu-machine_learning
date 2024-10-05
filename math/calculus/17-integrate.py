#!/usr/bin/env python3
"""
Module for calculating the integral of a polynomial
"""


def poly_integral(poly, C=0):
    """
    Calculates the integral of a polynomial represented
    as a list of coefficients

    Args:
        poly (list): List of coefficients representing the polynomial
        C (int, optional): Integration constant. Defaults to 0

    Returns:
        list: List of coefficients representing the integral
        of the polynomial, or None if invalid
    """
    # Input validation
    if not isinstance(
            poly, list) or not isinstance(
            C, (int, float)) or not poly:
        return None
    if not all(isinstance(c, (int, float)) for c in poly):
        return None

    integrals = [C]  # Initialize the integral list with constant C
    for power, coefficient in enumerate(poly):
        if power == 0:
            # The integral of a constant is the constant times x
            integrals.append(coefficient)
        else:
            # Calculate the integral coefficient
            integral = coefficient / (power + 1)
            integrals.append(
                # Store as int if it's whole
                int(integral) if integral.is_integer() else integral
            )
    # Remove trailing zeros
    while integrals[-1] == 0 and len(integrals) > 1:
        integrals.pop()
    return integrals
