#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(5)

# Generates 2000 random samples from a standard normal distribution and
# scales them by 10
x = np.random.randn(2000) * 10
y = np.random.randn(2000) * 10

# Generates 2000 random samples from a uniform distribution between 0 and
# 1, adds 40, and subtracts the distance from the origin
z = np.random.rand(2000) + 40 - np.sqrt(np.square(x) + np.square(y))

# the color of each data point is determined by the corresponding value in the z array
# cmap='viridis' argument specifies the colormap to use
plt.scatter(x, y, c=z, cmap='viridis')
plt.xlabel('x coordinate (m)')
plt.ylabel('y coordinate (m)')
plt.title('Mountain Elevation')

# Adds a colorbar to the plot and sets its label
plt.colorbar(label='elevation (m)')
plt.show()
