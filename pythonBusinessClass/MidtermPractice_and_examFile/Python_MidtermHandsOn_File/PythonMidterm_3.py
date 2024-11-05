"""
PythonMidterm_3.py

This program defines a Circle class that calculates the area and circumference of a circle
using a predefined radius. It then creates an instance of the Circle class and prints the 
calculated area and circumference.

Features:
    - Circle class with methods to calculate area and circumference using numpy's pi for accuracy
    - Instance creation and display of the calculated values for a circle with radius 5

Libraries Used:
    - numpy: Provides a precise value for pi used in calculations.

Usage:
    - This script demonstrates basic object-oriented programming principles and mathematical calculations.
"""

import numpy as np  # Importing numpy to use np.pi for precision

class Circle:
    def __init__(self, radius):
        """Initialize the Circle with a given radius."""
        self.radius = radius

    def calculate_area(self):
        """Calculate and return the area of the circle."""
        return np.pi * self.radius ** 2  # Using numpy's pi for precise calculation

    def calculate_circumference(self):
        """Calculate and return the circumference of the circle."""
        return 2 * np.pi * self.radius  # Using numpy's pi for precise calculation

# Create a Circle instance with a radius of 5
my_circle = Circle(5)

# Calculate area and circumference
area = my_circle.calculate_area()
circumference = my_circle.calculate_circumference()

# Display the results
print("The area of the circle is:", area)
print("The circumference of the circle is:", circumference)
