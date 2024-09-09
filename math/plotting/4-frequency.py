#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

# Setting a seed for reproducibility of results
np.random.seed(5)

# Generating 50 random student grades using a normal distribution
# with a mean of 68 and a standard deviation of 15
student_grades = np.random.normal(68, 15, 50)

# Plotting the histogram
plt.hist(student_grades, bins=range(0, 101, 10), edgecolor='black')

plt.xlabel('Grades')
plt.ylabel('Number of Students')
plt.title('Project A')
plt.show()
