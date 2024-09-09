#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(5)

# Generates a 4x3 random integer matrix where each element is between 0 and 19 (inclusive), representing the number of different fruits for each person
fruit = np.random.randint(0, 20, (4,3))

labels = ['Farrah', 'Fred', 'Felicia']
colors = ['red', 'yellow', 'orange', 'peach']

plt.figure(figsize=(8, 6)) # creates a figure with a specified size

# creates a bar plot. The first argument is the x-axis labels, second argument is the height of the bars, color argument specifies the color, the width argument specifies the width of the bars, and the bottom argument specifies the starting point for the bar (used for stacking)
plt.bar(labels, fruit[0], color=colors[0], width=0.5, label=colors[0])
plt.bar(labels, fruit[1], color=colors[1], width=0.5, label=colors[1], bottom=fruit[0])
plt.bar(labels, fruit[2], color=colors[2], width=0.5, label=colors[2], bottom=fruit[0] + fruit[1])
plt.bar(labels, fruit[3], color=colors[3], width=0.5, label=colors[3], bottom=fruit[0] + fruit[1] + fruit[2])

plt.xlabel('Person')
plt.ylabel('Quantity of Fruit')
plt.title('Number of Fruit per Person')
plt.ylim(0, 80)
plt.yticks(range(0, 81, 10))
plt.legend()
plt.show()
