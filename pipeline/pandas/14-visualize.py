#!/usr/bin/env python3

from datetime import date
import matplotlib.pyplot as plt
import pandas as pd
from_file = __import__('2-from_file').from_file

df = from_file('coinbaseUSD_1-min_data_2014-12-01_to_2019-01-09.csv', ',')

# Step 1: Remove the Weighted_Price column
df = df.drop(columns=['Weighted_Price'])

# Step 2: Rename the Timestamp column to Date
df = df.rename(columns={'Timestamp': 'Date'})

# Step 3: Convert the Date column to datetime
df['Date'] = pd.to_datetime(df['Date'], unit='s')

# Step 4: Set the Date as the DataFrame index
df.set_index('Date', inplace=True)

# Step 5: Handle missing values
df['Close'] = df['Close'].fillna(method='ffill')
df['High'] = df['High'].fillna(df['Close'])
df['Low'] = df['Low'].fillna(df['Close'])
df['Open'] = df['Open'].fillna(df['Close'])
df['Volume_(BTC)'] = df['Volume_(BTC)'].fillna(0)
df['Volume_(Currency)'] = df['Volume_(Currency)'].fillna(0)

# Step 6: Filter data from 2017 onward
df = df[df.index.year >= 2017]

# Step 7: Group by day and calculate the required aggregations
daily_df = df.resample('D').agg({
    'High': 'max',
    'Low': 'min',
    'Open': 'mean',
    'Close': 'mean',
    'Volume_(BTC)': 'sum',
    'Volume_(Currency)': 'sum'
})

# Step 8: Plot the data (for example, plotting Close price)
plt.figure(figsize=(10, 6))
plt.plot(daily_df.index, daily_df['Close'], label='Close Price', color='blue')
plt.title('Daily Close Price from 2017 Onward')
plt.xlabel('Date')
plt.ylabel('Close Price (USD)')
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()

# Show the plot
plt.show()