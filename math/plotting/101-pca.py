# Import necessary libraries
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

# Load the Iris flower data from pca.npz file (assuming the file is in ./data/)
data = np.load('./data/pca.npz/data.npy')
labels = np.load('./data/pca.npz/labels.npy')

# Center the data by subtracting the mean of each feature
data_means = np.mean(data, axis=0)
norm_data = data - data_means

# Perform PCA (Principal Component Analysis) to reduce dimensionality to 3
# This involves Singular Value Decomposition (SVD)
_, _, Vh = np.linalg.svd(norm_data)
# Project data onto first 3 principal components
pca_data = np.matmul(norm_data, Vh[:3].T)

# Create a 3D scatter plot figure
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1, projection='3d')  # Create a 3D subplot

# Scatter plot the data points colored by their species labels (using
# 'plasma' colormap)
ax.scatter(
    pca_data[:, 0],  # x-axis: values from first principal component
    pca_data[:, 1],  # y-axis: values from second principal component
    pca_data[:, 2],  # z-axis: values from third principal component
    c=labels,        # Color based on species labels
    label=labels,     # Add labels for each data point (optional)
    cmap=plt.get_cmap('plasma'),  # Use 'plasma' colormap for color gradient
)

# Set labels for the axes
ax.set_xlabel('U1')
ax.set_ylabel('U2')
ax.set_zlabel('U3')  # U1, U2, and U3 are the first three principal components

# Set the title of the plot
plt.title("PCA of Iris Dataset")

# Show the plot
plt.show()
