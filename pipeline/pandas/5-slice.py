#!/usr/bin/env python3

import pandas as pd
from_file = __import__('2-from_file').from_file

df = from_file('coinbaseUSD_1-min_data_2014-12-01_to_2019-01-09.csv', ',')

# Slice the DataFrame: specific columns and every 60th row
df = df.loc[::60, ['High', 'Low', 'Close', 'Volume_(BTC)']]

print(df.tail())
