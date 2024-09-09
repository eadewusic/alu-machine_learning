#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

# creates a NumPy array, np.arange function takes two arguments: 0 and the ending value (exclusive)
# ** 3 cubes each number - instead of 0 - 10, it will be 0, 1, 8, 27 - 729
y = np.arange(0, 11) ** 3

# linestyle='-' with colour specified or 'r-' is to make a solid red line
plt.plot(y, 'r-')
plt.xlim(0, 10)  # Set x-axis range from 0 to 10
plt.show()
