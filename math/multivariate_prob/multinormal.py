#!/usr/bin/env python3
"""
This module contains the class MultiNormal
to represent a Multivariate Normal distribution
"""

import numpy as np

class MultiNormal:
    """
    Represents a Multivariate Normal distribution
    """
    def __init__(self, data):
        """
        Initializes the MultiNormal instance

        Parameters:
        data (numpy.ndarray): A 2D array of shape (d, n)
        containing the dataset
        
        Raises:
        TypeError: If data is not a 2D numpy.ndarray
        ValueError: If data contains less than 2 data points
        """
        # Check if data is a 2D numpy.ndarray
        if not isinstance(data, np.ndarray) or data.ndim != 2:
            raise TypeError("data must be a 2D numpy.ndarray")
        
        # Check if n (number of data points) is less than 2
        d, n = data.shape
        if n < 2:
            raise ValueError("data must contain multiple data points")
        
        # Calculate the mean (shape (d, 1))
        self.mean = np.mean(data, axis=1, keepdims=True)

        # Center the data by subtracting the mean from each data point
        centered_data = data - self.mean
        
        # Calculate the covariance matrix (shape (d, d))
        self.cov = np.dot(centered_data, centered_data.T) / (n - 1)

    def pdf(self, x):
        """
        Calculates the PDF at a data point

        Parameters:
        x (numpy.ndarray): A data point of shape (d, 1)
        whose PDF should be calculated
        
        Returns:
        float: The value of the PDF at the data point
        
        Raises:
        TypeError: If x is not a numpy.ndarray
        ValueError: If x does not have shape (d, 1)
        """
        # Check if x is a numpy.ndarray
        if not isinstance(x, np.ndarray):
            raise TypeError("x must be a numpy.ndarray")
        
        # Check if x has the correct shape (d, 1)
        d = self.mean.shape[0]
        if x.shape != (d, 1):
            raise ValueError(f"x must have the shape ({d}, 1)")
        
        # Calculate the determinant and inverse of the covariance matrix
        det_cov = np.linalg.det(self.cov)
        inv_cov = np.linalg.inv(self.cov)
        
        # Calculate the normalization factor
        norm_factor = 1 / np.sqrt(((2 * np.pi) ** d) * det_cov)
        
        # Center the point x by subtracting the mean
        x_centered = x - self.mean
        
        # Calculate the exponent part
        exponent = -0.5 * np.dot(np.dot(x_centered.T, inv_cov), x_centered)
        
        # Return the PDF value
        pdf_value = norm_factor * np.exp(exponent)
        
        # Since pdf_value is a 1x1 matrix, return the scalar
        return pdf_value[0, 0]
