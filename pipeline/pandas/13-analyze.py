#!/usr/bin/env python3

import pandas as pd
from_file = __import__('2-from_file').from_file

# Load the data
df = from_file('coinbaseUSD_1-min_data_2014-12-01_to_2019-01-09.csv', ',')

# Exclude the 'Timestamp' column and calculate descriptive statistics for the remaining columns
stats = df.drop(columns=['Timestamp']).describe()

# Print the stats
print(stats)
