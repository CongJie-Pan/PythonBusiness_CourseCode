import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans

# Load the data from the CSV file
data = pd.read_csv("dataCSV.csv")
print(data)

# Plot the scatter plot with default color (red) for all points
plt.scatter(data.X, data.Y, c="red")
plt.title('Scatter Plot with Default Color (Red)')
plt.show()

# Run KMeans clustering
kmeans = KMeans(n_clusters=4)  # Using 3 clusters for this example
kmeans.fit(data[['X', 'Y']])  # Fit KMeans to the data (X and Y)

# Get the cluster labels (which cluster each point belongs to)
clusters = kmeans.labels_

# Define colors for clusters (for example: 0 -> red, 1 -> yellow)
colors = np.array(["red", "yellow", "blue", "green"])

# Plot scatter plot with different colors based on KMeans clustering
plt.scatter(data.X, data.Y, c=colors[clusters])
plt.title('Scatter Plot with KMeans Clustering')
plt.show()
