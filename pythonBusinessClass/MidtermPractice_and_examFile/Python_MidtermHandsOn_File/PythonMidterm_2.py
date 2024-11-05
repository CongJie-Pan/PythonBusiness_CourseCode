"""
PythonMidterm_2.py

This program creates a scatter plot using a predefined set of data points and applies KMeans clustering
to classify them into different groups. The clustering results are visualized in a scatter plot where each
cluster is represented by a different color.

Libraries Used:
    - matplotlib.pyplot: For creating and displaying scatter plots
    - pandas: For organizing data in a structured format using DataFrames
    - numpy: For generating random numbers (only if required to generate data dynamically)
    - sklearn.cluster.KMeans: For applying the KMeans clustering algorithm

Functionality:
    - The code includes a set of X and Y coordinates for 12 data points.
    - A scatter plot is generated to display these points in red.
    - KMeans clustering is applied to group the points into 3 clusters, with each cluster displayed in a different color.

Usage Notes:
    - The code currently uses predefined points for plotting.
    - Adjust the number of clusters in KMeans if needed.
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans

# Predefined values for X and Y coordinates as fixed points
x_values = [1, 2, 2.5, 1.5, 6, 7, 7.5, 6.5, 8, 9, 10, 5]
y_values = [2, 3, 2.5, 3.5, 4, 8, 7, 9, 8.5, 10, 5, 6]

# Convert fixed values into a DataFrame for easy plotting and handling
data = pd.DataFrame({'X': x_values, 'Y': y_values})

# Plot the scatter plot with the fixed points in red
plt.scatter(data['X'], data['Y'], c="red")
plt.title('Scatter Plot with 12 Predefined Points')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()

# Apply KMeans clustering
kmeans = KMeans(n_clusters=3, random_state=42)  # Setting 3 clusters as example
data['Cluster'] = kmeans.fit_predict(data[['X', 'Y']])  # Adding cluster labels to DataFrame

# Define colors for clusters (0 -> red, 1 -> yellow, 2 -> blue)
colors = np.array(["red", "yellow", "blue"])

# Plot scatter plot with different colors based on KMeans clustering
plt.scatter(data['X'], data['Y'], c=colors[data['Cluster']])
plt.title('KMeans Clustering of Points into 3 Groups')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()
