#!/usr/bin/env python3

import pandas as pd
from_file = __import__('2-from_file').from_file

df = from_file('coinbaseUSD_1-min_data_2014-12-01_to_2019-01-09.csv', ',')

# Reverse the rows (reverse chronological order)
df = df[::-1]

# Transpose the DataFrame
df = df.transpose()

print(df.tail(8))
