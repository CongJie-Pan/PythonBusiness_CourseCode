# The code loads the classic Iris dataset using scikit-learn's built-in dataset loader and extracts features, target values, and names.
# It creates a scatter plot comparing sepal length versus sepal width for different iris species, with each species shown in a different color.
# The code then builds a decision tree classifier with a maximum depth of 3 and trains it on the Iris dataset.
# Finally, it visualizes the trained decision tree using matplotlib, showing how the model splits the data based on different feature thresholds to classify iris species.


from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier, plot_tree
import matplotlib.pyplot as plt
import seaborn as sns

# Load the Iris dataset
data = load_iris()
X = data.data
y = data.target
feature_names = data.feature_names
target_names = data.target_names

# Scatter plot: petal length vs petal width
plt.figure(figsize=(8, 6))
for i, target_name in enumerate(target_names):
    plt.scatter(
        X[y == i, 0], X[y == i, 1],
        label=target_name, alpha=0.7, edgecolors='k'
    )
plt.title("Iris Dataset: Sepal Length vs Sepal Width")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Sepal Width (cm)")
plt.legend()
plt.show()

# Load dataset
data = load_iris()
X, y = data.data, data.target

# Create and train the model
model = DecisionTreeClassifier(max_depth=3, random_state=42)
model.fit(X, y)

# Visualize the tree
plt.figure(figsize=(12, 8))
plot_tree(
    model,
    feature_names=data.feature_names,
    class_names=data.target_names.tolist(),  # Convert to list
    filled=True
)
plt.show()

# Load dataset
data = load_iris()
X, y = data.data, data.target

# Create and train the model
model = DecisionTreeClassifier(max_depth=3, random_state=42)
model.fit(X, y)

# Visualize the tree
plt.figure(figsize=(12, 8))
plot_tree(
    model,
    feature_names=data.feature_names,
    class_names=data.target_names.tolist(),  # Convert to list
    filled=True
)
plt.show()
