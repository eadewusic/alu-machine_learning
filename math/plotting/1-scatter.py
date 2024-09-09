#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

# mean of the distribution - height ininches, weight in pounds
mean = [69, 0]

# covariance matrix of the distribution, shows relationship between height
# and weight
cov = [[15, 8], [8, 15]]

# sets random seed to 5, ensuring that the same random numbers are
# generated each time the code is run
np.random.seed(5)

# generates 2000 random samples from the distribution with the specified
# mean and covariance. T transposes (swaps rows and columns) the result,
# so x contains the height values and y contains the weight values
x, y = np.random.multivariate_normal(mean, cov, 2000).T

# shifts the weight values upward by 180 pounds
y += 180

plt.scatter(x, y, color='magenta')
plt.xlabel('Height (in)')
plt.ylabel('Weight (lbs)')
plt.title('Men\'s Height vs Weight')
plt.show()
