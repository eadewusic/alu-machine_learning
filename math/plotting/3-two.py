#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

# Generate values for x from 0 to 20000 in steps of 1000
x = np.arange(0, 21000, 1000)

# Natural logarithm of 0.5 (used to calculate the decay rate)
r = np.log(0.5)

# Half-life of C-14 (5730 years)
t1 = 5730

# Half-life of Ra-226 (1600 years)
t2 = 1600

# Calculate the fraction remaining for C-14 over time
y1 = np.exp((r / t1) * x)

# Calculate the fraction remaining for Ra-226 over time
y2 = np.exp((r / t2) * x)

# Plot y1 with a dashed red line
plt.plot(x, y1, 'r--', label='C-14')

# Plot y2 with a solid green line
plt.plot(x, y2, 'g-', label='Ra-226')

plt.xlabel('Time (years)')
plt.ylabel('Fraction Remaining')
plt.title('Exponential Decay of Radioactive Elements')
plt.xlim([0, 20000])
plt.ylim([0, 1])

# Add a legend (informative square of plot) to the top right corner of the plot
plt.legend(loc='upper right')

plt.show()
