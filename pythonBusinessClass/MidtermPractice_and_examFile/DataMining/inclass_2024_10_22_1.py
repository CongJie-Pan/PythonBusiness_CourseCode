import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# ELBOW Method

# Step 1: Load your CSV data
data = pd.read_csv('dataCSV.csv')

# Step 2: Extract relevant columns (assuming your file has 'X' and 'Y' columns)
X = data[['X', 'Y']]  # Select only the X and Y columns for clustering

# Step 3: Calculate WCSS for different number of clusters
wcss = []
max_clusters = min(10, len(X))  # Make sure K is <= the number of data points
for i in range(1, max_clusters + 1):  # Try cluster numbers from 1 to the number of data points or 10
    kmeans = KMeans(n_clusters=i, init='k-means++', max_iter=300, n_init=10, random_state=0)
    kmeans.fit(X)  # Fit KMeans on the data
    wcss.append(kmeans.inertia_)  # Inertia represents WCSS

# Step 4: Plot the WCSS to visualize the Elbow
plt.plot(range(1, max_clusters + 1), wcss)
plt.title('Elbow Method')
plt.xlabel('Number of Clusters (K)')
plt.ylabel('WCSS (Within-Cluster Sum of Square)')
plt.show()
