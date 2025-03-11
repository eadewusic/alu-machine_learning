#!/usr/bin/env python3
"""Load data from a file and return as a pandas DataFrame"""

import pandas as pd

def from_file(filename, delimiter):
    """
    Loads data from a file into a pandas DataFrame.

    Args:
        filename (str): The path to the file to load.
        delimiter (str): The delimiter used in the file.

    Returns:
        pd.DataFrame: The resulting DataFrame containing the data.
    """
    return pd.read_csv(filename, delimiter=delimiter)
