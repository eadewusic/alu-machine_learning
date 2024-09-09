#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

# creates a NumPy array x containing values from 0 to 28650 in steps of 5730
x = np.arange(0, 28651, 5730)

# calculates the decay constant for carbon-14
r = np.log(0.5)

t = 5730  # half-life of carbon-14

# calculate the fraction remaining of carbon-14 at each time point using
# the exponential decay formula: y = e^(rt), where r is the decay
# constant, t is the time, and y is the fraction remaining
y = np.exp((r / t) * x)

plt.plot(x, y)
plt.xlabel('Time (years)')
plt.ylabel('Fraction Remaining')
plt.title('Exponential Decay of C-14')
# sets y-axis to logarithmic scale appropriate for exponential decay
plt.yscale('log')
plt.xlim(0, 28650)
plt.show()
