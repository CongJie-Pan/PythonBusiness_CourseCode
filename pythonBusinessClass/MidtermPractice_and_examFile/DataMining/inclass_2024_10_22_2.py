from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Load the Iris dataset
iris = load_iris()

# Create a DataFrame
data = pd.DataFrame(iris.data, columns=iris.feature_names)

# Apply KMeans with 3 clusters (since we know there are 3 species)
kmeans = KMeans(n_clusters=3)
data['cluster'] = kmeans.fit_predict(iris.data)

# Map the actual species names for comparison
data['species'] = iris.target
data['species'] = data['species'].map({0: 'setosa', 1: 'versicolor', 2: 'virginica'})

# Visualize the clustering results with a scatter plot (sepal length vs. sepal width)
plt.figure(figsize=(8, 6))
sns.scatterplot(x='sepal length (cm)', y='sepal width (cm)', hue='cluster', data=data, palette='deep')
plt.title('KMeans Clustering of Iris Dataset (Sepal Length vs Sepal Width)')
plt.show()