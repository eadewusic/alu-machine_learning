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

# define main figure and create the 3x2 grid layout for subplots
fig = plt.figure(figsize=(10, 8))
grid = plt.GridSpec(3, 2, figure=fig)

# First subplot
ax1 = fig.add_subplot(grid[0, 0])
ax2 = fig.add_subplot(grid[0, 1])
ax3 = fig.add_subplot(grid[1, 0])
ax4 = fig.add_subplot(grid[1, 1])
ax5 = fig.add_subplot(grid[2, :])

ax1.set_xlim(0, 10)
ax1.set_yticks(range(0, 1001, 500))
ax1.set_ylim(0, 1000)
ax1.plot(y0, 'r')

# Second subplot
ax2.scatter(x1, y1, c='magenta')
ax2.set_ylabel('Weight (lbs)')
ax2.set_xlabel('Height (in)')
ax2.set_xticks([60, 70, 80])
ax2.set_title('Men\'s Height vs Weight')

# Third subplot
ax3.plot(x2, y2)
ax3.set_xlabel('Time (years)')
ax3.set_ylabel('Fraction remaining')
ax3.set_title('Exponential Decay of C-14')
ax3.set_yscale('log')
ax3.set_xlim(0, 28650)

# Fourth subplot
ax4.plot(x3, y31, 'r--', label="C-14")
ax4.plot(x3, y32, 'g', label="Ra-226")
ax4.set_xlabel('Time (years)')
ax4.set_ylabel('Fraction Remaining')
ax4.set_title('Exponential Decay of Radioactive Elements')
ax4.set_xlim(0, 20000)
ax4.set_xticks(range(0, 20001, 5000))
ax4.set_ylim(0, 1)
ax4.legend()

# Fifth subplot
ax5.hist(student_grades, bins=range(0, 101, 10), edgecolor='black')
ax5.set_xlabel("Grades")
ax5.set_ylabel("Number of Students")
ax5.set_title("Project A")
ax5.set_ylim(0, 30)
ax5.set_xlim(0, 100)

# specify positions of the x-axis ticks in the subplot
ax5.set_xticks(np.arange(0, 101, 10))

# Adjust plots layout to prevent overlap and ensure all plot elements fit within the figure boundaries
# 0, 0 is lower left corner; 1, 0.95 is upper right corner
# rect specifies that the subplots should occupy the entire width of the
# figure (from 0 to 1) and 95% of the height (from 0 to 0.95) which
# reduces the top margin of the figure, preventing the title from
# overlapping with the subplots
plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.suptitle("All in One")

# Adjust font size for axes labels and titles
for ax in fig.get_axes():
    ax.xaxis.label.set_size('x-small')
    ax.yaxis.label.set_size('x-small')
    ax.title.set_size('x-small')

plt.show()
