# The code imports necessary libraries and loads the Iris dataset, converting it into pandas DataFrames and splitting it into training (80%) and testing (20%) sets.
# It creates and trains a decision tree classifier on the training data, then visualizes the resulting tree structure.
# The model makes predictions on the test set using the trained decision tree classifier.
# Finally, it evaluates the model's performance using multiple metrics: accuracy score (showing overall correctness), confusion matrix (showing prediction errors across classes), and a classification report (showing precision, recall, and F1-score for each class).IrisDataAnalyzing_1.py

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier, plot_tree
#
data = load_iris()
X = pd.DataFrame(data.data, columns=data.feature_names)
y = pd.Series(data.target, name="target")
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
#
tree_model = DecisionTreeClassifier()
tree_model.fit(X_train, y_train)

# Visualize the tree
plt.figure(figsize=(12, 8))
plot_tree(
    tree_model,
    feature_names=data.feature_names,
    class_names=data.target_names.tolist(),  # Convert to list
    filled=True
)
plt.show()

# Predict on the test set
y_pred = tree_model.predict(X_test)

# 1. Accuracy score
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.2f}")

# 2. Confusion matrix
cm = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:")
print(cm)

# 3. Classification report (Precision, Recall, F1-score)
cr = classification_report(y_test, y_pred, target_names=data.target_names)
print("Classification Report:")
print(cr)
