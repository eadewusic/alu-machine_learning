#!/usr/bin/env python3
"""Create a pandas DataFrame from a 
dictionary with specific row labels"""

import pandas as pd

# Define the data as a dictionary
data = {
    'First': [0.0, 0.5, 1.0, 1.5],
    'Second': ['one', 'two', 'three', 'four']
}

# Create the DataFrame with custom index labels
df = pd.DataFrame(data, index=['A', 'B', 'C', 'D'])
