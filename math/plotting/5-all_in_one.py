#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

# Data for the plots
y0 = np.arange(0, 11) ** 3

mean = [69, 0]
cov = [[15, 8], [8, 15]]
np.random.seed(5)
x1, y1 = np.random.multivariate_normal(mean, cov, 2000).T
y1 += 180

x2 = np.arange(0, 28651, 5730)
r2 = np.log(0.5)
t2 = 5730
y2 = np.exp((r2 / t2) * x2)

x3 = np.arange(0, 21000, 1000)
r3 = np.log(0.5)
t31 = 5730
t32 = 1600
y31 = np.exp((r3 / t31) * x3)
y32 = np.exp((r3 / t32) * x3)

np.random.seed(5)
student_grades = np.random.normal(68, 15, 50)

# Creating the 3x2 grid layout for subplots
fig, axs = plt.subplots(3, 2, figsize=(10, 8))
fig.suptitle('All in One')

# First subplot
axs[0, 0].plot(np.arange(0, 11), y0, 'r')

# Second subplot
axs[0, 1].scatter(x1, y1, c='magenta')
axs[0, 1].set_title("Men's Height vs Weight", fontsize='x-small')
axs[0, 1].set_xlabel('Height (in)', fontsize='x-small')
axs[0, 1].set_ylabel('Weight (lbs)', fontsize='x-small')

# Third subplot
axs[1, 0].plot(x2, y2)
axs[1, 0].set_yscale('log')
axs[1, 0].set_title('Exponential Decay of C-14', fontsize='x-small')
axs[1, 0].set_xlabel('Time (years)', fontsize='x-small')
axs[1, 0].set_ylabel('Fraction Remaining', fontsize='x-small')

# Fourth subplot
axs[1, 1].plot(x3, y31, 'r--', label='C-14')
axs[1, 1].plot(x3, y32, 'g-', label='Ra-226')
axs[1, 1].set_title('Exponential Decay of Radioactive Elements', fontsize='x-small')
axs[1, 1].set_xlabel('Time (years)', fontsize='x-small')
axs[1, 1].set_ylabel('Fraction Remaining', fontsize='x-small')
axs[1, 1].legend(loc='upper right', fontsize='x-small')

# Fifth subplot (on left column)
# axs[2, 0].hist(student_grades, bins=10, edgecolor='black')
# axs[2, 0].set_title('Project A', fontsize='x-small')
# axs[2, 0].set_xlabel('Grades', fontsize='x-small')
# axs[2, 0].set_ylabel('Number of Students', fontsize='x-small')
# axs[2, 1].remove() Remove the second subplot in the last row

# Fifth subplot spanning two columns and centralised

# the subplot ax5 span both columns in the last row by specifying it as (5, 6), this spanning automatically centers it horizontally
ax5 = fig.add_subplot(3, 2, (5, 6)) 
ax5.hist(student_grades, bins=10, edgecolor='black')
ax5.set_title('Project A', fontsize='x-small')
ax5.set_xlabel('Grades', fontsize='x-small')
ax5.set_ylabel('Number of Students', fontsize='x-small')

# Adjust layout to prevent overlap
plt.tight_layout() #ensure plots do not overlap 
plt.subplots_adjust(top=0.9) # makes sure title fits well

plt.show()
