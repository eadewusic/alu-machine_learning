#!/usr/bin/env python3
"""
This module contains the class MultiNormal to 
represent a Multivariate Normal distribution
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
        data (numpy.ndarray): A 2D array of shape (d, n) containing the dataset
        
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
