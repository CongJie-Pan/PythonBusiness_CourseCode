'''
Create a Python program that reads two text files: names.txt and girl_names.txt.
The program should count how many names from names.txt match the names listed in girl_names.txt.
After that, display the matching names and the total count.

Expected Output:
- A list of names that appear in both files.
- The total count of matching names.

'''

import tkinter as tk
from tkinter import messagebox, Toplevel
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def read_names_from_file(file_name):
    """Read the file and return a list of names"""
    # Open the specified file in read mode
    with open(file_name, "r") as file:
        # Read all lines in the file, remove newline characters, and return a list of names
        return file.read().splitlines()  # Returns the list directly without needing additional steps

def count_girls_names(names, girl_names):
    """Count and return matching girl names"""
    # Create a list of names that exist in both 'names' and 'girl_names'
    # This uses a list comprehension to filter names that are also in the girl_names list
    matched_names = [name for name in names if name in girl_names]
    return matched_names  # Return the list of matched names

# Read the names from the file "names.txt" which contains a list of names
names = read_names_from_file('names.txt')
# Read the names from the file "GirlNames.txt" which contains known girl names
girl_names = read_names_from_file('GirlNames.txt')

# Use the count_girls_names function to find matching names between the two lists
matched_names = count_girls_names(names, girl_names)

# Output the result to the console
print(f"Number of matching girl names: {len(matched_names)}")  # Print the total count of matched names
print("The matching girl names are:")

# Enumerate over the matched names to display each name with a sequence number
for i, name in enumerate(matched_names, start=1):
    print(f"({i}) {name}")  # Print each name on a new line, adding the sequence number for readability
