from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

# Load the Iris flower data from pca.npz
# lib = np.load("./data/pca.npz")
data = np.load('./data/pca.npz/data.npy')
labels = np.load('./data/pca.npz/labels.npy')

# Center the data
data_means = np.mean(data, axis=0)
norm_data = data - data_means

# Perform PCA to reduce dimensionality to 3
_, _, Vh = np.linalg.svd(norm_data)
pca_data = np.matmul(norm_data, Vh[:3].T)

# Create the 3D scatter plot
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection='3d')

# Plot the data points colored by their species
colors = plt.cm.plasma(labels)  # Use plasma colormap
scatter = ax.scatter(pca_data[:, 0], pca_data[:, 1],
                     pca_data[:, 2], c=colors, s=50)

# Create a dummy ScalarMappable object
norm = plt.Normalize(vmin=min(labels), vmax=max(labels)
                     )  # Assuming labels range from 0-2
sm = plt.cm.ScalarMappable(cmap=plt.cm.plasma, norm=norm)
sm.set_array([])  # Set an empty array

# Set labels and title
ax.set_xlabel('U1')
ax.set_ylabel('U2')
ax.set_zlabel('U3')
ax.set_title('PCA of Iris Dataset')

# Add a colorbar with the dummy mappable
plt.colorbar(sm, label='Species')

# Show the plot
plt.show()
