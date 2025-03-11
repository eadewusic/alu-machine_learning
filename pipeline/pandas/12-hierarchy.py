#!/usr/bin/env python3

import pandas as pd
from_file = __import__('2-from_file').from_file

# Load the data
df1 = from_file('coinbaseUSD_1-min_data_2014-12-01_to_2019-01-09.csv', ',')
df2 = from_file('bitstampUSD_1-min_data_2012-01-01_to_2020-04-22.csv', ',')

# Convert the Timestamp to datetime for filtering
df1['Timestamp'] = pd.to_datetime(df1['Timestamp'], unit='s')
df2['Timestamp'] = pd.to_datetime(df2['Timestamp'], unit='s')

# Filter the data based on the given timestamps
start_timestamp = pd.to_datetime(1417411980, unit='s')
end_timestamp = pd.to_datetime(1417417980, unit='s')

df1_filtered = df1[(df1['Timestamp'] >= start_timestamp) & (df1['Timestamp'] <= end_timestamp)]
df2_filtered = df2[(df2['Timestamp'] >= start_timestamp) & (df2['Timestamp'] <= end_timestamp)]

# Add a key column for identification
df1_filtered['Source'] = 'coinbase'
df2_filtered['Source'] = 'bitstamp'

# Concatenate the two dataframes
df = pd.concat([df1_filtered, df2_filtered])

# Set the MultiIndex with Timestamp and Source
df.set_index(['Timestamp', 'Source'], inplace=True)

# Sort the data by Timestamp
df.sort_index(inplace=True)

# Display the result
print(df)
