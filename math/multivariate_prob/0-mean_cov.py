import numpy as np

def mean_cov(X):
    """
    Calculates the mean and covariance of a dataset.
    
    Parameters:
    X (numpy.ndarray): A 2D array of shape (n, d) containing the dataset.

    Returns:
    tuple: A tuple containing:
        - mean (numpy.ndarray): The mean of the dataset of shape (1, d).
        - cov (numpy.ndarray): The covariance matrix of shape (d, d).
    
    Raises:
    TypeError: If X is not a 2D numpy.ndarray.
    ValueError: If X contains less than 2 data points.
    """
    # Check if X is a 2D numpy.ndarray
    if not isinstance(X, np.ndarray) or X.ndim != 2:
        raise TypeError("X must be a 2D numpy.ndarray")

    # Check if n is less than 2
    n, d = X.shape
    if n < 2:
        raise ValueError("X must contain multiple data points")

    # Calculate the mean
    mean = np.mean(X, axis=0).reshape(1, d)

    # Calculate the covariance matrix
    # Center the data
    centered_X = X - mean
    cov = np.dot(centered_X.T, centered_X) / (n - 1)

    return mean, cov
