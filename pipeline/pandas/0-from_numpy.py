#!/usr/bin/env python3
"""
This script defines a function that converts a NumPy array
into a Pandas DataFrame.
Each column in the DataFrame is labeled in alphabetical order from A to Z.
"""
import pandas as pd
import numpy as np


def from_numpy(array):
    """
    Creates a pd.DataFrame from a np.ndarray

    Parameters:
    array (np.ndarray): The input numpy array

    Returns:
    pd.DataFrame: The newly created DataFrame with columns labeled A-Z
    """
    num_cols = array.shape[1]  # Get number of columns
    columns = [chr(65 + i)
               for i in range(num_cols)]  # Generate column names A-Z
    return pd.DataFrame(array, columns=columns)


# Testing the function
if __name__ == "__main__":
    np.random.seed(0)
    A = np.random.randn(5, 8)
    print(from_numpy(A))

    B = np.random.randn(9, 3)
    print(from_numpy(B))
