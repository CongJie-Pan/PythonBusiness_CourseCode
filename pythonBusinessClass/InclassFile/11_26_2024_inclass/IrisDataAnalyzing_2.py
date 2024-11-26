# The code imports necessary libraries and loads the Iris dataset, organizing it into pandas DataFrames and splitting it into training (80%) and testing (20%) sets.
# It creates and trains a Random Forest classifier with 100 decision trees, using random_state=45 for reproducibility.
# The model makes predictions on the test set using the trained Random Forest model.
# Finally, it evaluates the model's performance using the same metrics as before (accuracy score, confusion matrix, and classification report) to assess how well the Random Forest classifier performs on unseen data.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

# Load the Iris dataset
data = load_iris()
X = pd.DataFrame(data.data, columns=data.feature_names)
y = pd.Series(data.target, name="target")

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train the Random Forest model
rf_model = RandomForestClassifier(n_estimators=100, random_state=45)
rf_model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = rf_model.predict(X_test)

# Evaluate the model
print(f"Accuracy: {accuracy_score(y_test, y_pred):.2f}")
print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))
print("Classification Report:")
print(classification_report(y_test, y_pred, target_names=data.target_names))
