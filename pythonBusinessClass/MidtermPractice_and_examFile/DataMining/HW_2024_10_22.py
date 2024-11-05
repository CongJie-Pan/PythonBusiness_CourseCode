import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans

# Set a seed for reproducibility, delete it can produce the points randomly
# np.random.seed(42)

# Generate random data
random_data = {
    'X': np.random.rand(30) * 50,  # Random values between 0 and 10 for X
    'Y': np.random.rand(30) * 50   # Random values between 0 and 10 for Y
}

# Convert the random data into a DataFrame
data = pd.DataFrame(random_data)

# Plot the scatter plot with default color (red) for all points
plt.scatter(data['X'], data['Y'], c="red")
plt.title('Scatter Plot with Default Color (Red)')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()

# Run KMeans clustering
kmeans = KMeans(n_clusters=4)  # Using 4 clusters for this example
kmeans.fit(data[['X', 'Y']])  # Fit KMeans to the data (X and Y)

# Get the cluster labels (which cluster each point belongs to)
clusters = kmeans.labels_

# Define colors for clusters (for example: 0 -> red, 1 -> yellow, etc.)
colors = np.array(["red", "yellow", "blue", "green"])

# Plot scatter plot with different colors based on KMeans clustering
plt.scatter(data['X'], data['Y'], c=colors[clusters])
plt.title('Scatter Plot with KMeans Clustering (30 random points)')
plt.xlabel('X')
plt.ylabel('Y')

plt.show()

