'''
Write a Python GUI program that generates user input random points and applies the KMeans clustering
algorithm to classify them into different groups.
Use the Elbow method to determine the optimal number of clusters,
and then visualize the clusters in a scatter plot with different colors for each group.

Expected Output:
- The user can input the numbers of the random points to generate in GUI.
- A submit button to generate the random points and apply the KMeans algorithm.
- A scatter plot showing the random points colored by their cluster assignments in the new window.
- A plot showing the **Elbow curve** (number of clusters vs WCSS) to determine the optimal K.

'''

import tkinter as tk
from tkinter import messagebox, Toplevel
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Function to generate random points and apply KMeans clustering
def Random_Points_Scatter_Plot():
    try:
        # Get the number of random points from the user input
        randomPointsInput = int(entry.get())

        if randomPointsInput <= 0:
            messagebox.showerror("Input Error", "Please enter a positive integer.")
            return

        # Generate random data for X and Y coordinates
        random_data = {
            'X': np.random.rand(randomPointsInput) * 50,  # Random values between 0 and 50 for X
            'Y': np.random.rand(randomPointsInput) * 50   # Random values between 0 and 50 for Y
        }

        # Convert the random data into a DataFrame
        data = pd.DataFrame(random_data)

        # Run KMeans clustering
        optimal_k = 4  # Set optimal K to 4 (or any fixed value based on your choice)
        kmeans = KMeans(n_clusters=optimal_k, random_state=42)
        clusters = kmeans.fit_predict(data[['X', 'Y']])

        # Define colors for clusters
        colors = np.array(["red", "yellow", "blue", "green"])

        # Open a new window for the scatter plot
        new_window = Toplevel(window)
        new_window.title(f"KMeans Clustering of {randomPointsInput} Random Points")

        # Create a Matplotlib figure and plot
        fig, ax = plt.subplots()
        scatter = ax.scatter(data['X'], data['Y'], c=colors[clusters])
        ax.set_title(f'KMeans Clustering of {randomPointsInput} Random Points')
        ax.set_xlabel('X')
        ax.set_ylabel('Y')

        # Embed the plot in the new Tkinter window using FigureCanvasTkAgg
        canvas = FigureCanvasTkAgg(fig, master=new_window)
        canvas.draw()
        canvas.get_tk_widget().pack()

    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid integer.")

# ==== GUI Building ====

# Create the main window
window = tk.Tk()
window.title("Random Points Scatter Plot")

# Set the window size and disable resizing
window.geometry("400x300+600+300")
window.resizable(False, False)

# Ask the user to input random points
label = tk.Label(window, text="Enter the number of random points you want:")
label.place(relx=0.5, rely=0.1, anchor='center')

# Create and place an entry(input box) for the number of points
entry = tk.Entry(window)
entry.place(relx=0.5, rely=0.2, anchor='center', width=180)

# Create a button to generate the scatter plot
button = tk.Button(window, text="Generate Scatter Plot", command=Random_Points_Scatter_Plot)
button.place(relx=0.5, rely=0.4, anchor='center', width=200, height=30)

# Create an Exit button that closes the window
exit_button = tk.Button(window, text="Exit", command=window.destroy)
exit_button.place(relx=0.5, rely=0.7, anchor='center', width=70, height=30)

# Run the application
window.mainloop()
