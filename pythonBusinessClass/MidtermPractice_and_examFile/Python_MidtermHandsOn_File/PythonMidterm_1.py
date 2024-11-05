"""
PythonMidterm_1.py

This program creates a scatter plot with a predefined set of data points using fixed arrays for X and Y coordinates.
It utilizes the following libraries:
    - matplotlib.pyplot: For creating and displaying scatter plots
    - pandas: For organizing data in a structured format using DataFrames

The program includes:
    - A predefined set of X and Y coordinates to form 12 data points
    - Conversion of these arrays into a pandas DataFrame for easier manipulation and plotting
    - Display of a scatter plot with all points in red

Usage:
    - This script does not include random data generation. It strictly uses predefined data arrays for consistent results.
"""

import matplotlib.pyplot as plt
import pandas as pd

# Predefined values for X and Y coordinates as fixed points
x_values = [1, 2, 2.5, 1.5, 6, 7, 7.5, 6.5, 8, 9, 10, 5]
y_values = [2, 3, 2.5, 3.5, 4, 8, 7, 9, 8.5, 10, 5, 6]

# ** Convert fixed values into a DataFrame for easy plotting and handling **
data = pd.DataFrame({'X': x_values, 'Y': y_values})

# Plot the scatter plot with the fixed points in red
plt.scatter(data['X'], data['Y'], c="red")
plt.title('Scatter Plot with 12 Predefined Points')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()
