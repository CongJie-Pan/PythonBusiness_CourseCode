"""
PythonMidterm_4.py

This program creates a simple GUI application that allows the user to enter a number
and increment or decrement the displayed number based on the entered value by clicking
the "Plus" or "Minus" buttons.

Features:
    - User input field for specifying the amount to change the current number
    - Plus and Minus buttons to add or subtract the entered value from the displayed number
    - Error handling for invalid input

Libraries Used:
    - tkinter: For GUI components and message boxes

"""

import tkinter as tk
from tkinter import messagebox

def update_number(is_addition):
    """
    Update the displayed number based on the user input and button clicked (Plus or Minus).

    Parameters:
    is_addition (bool): True if adding the number, False if subtracting
    """
    try:
        # Get the current displayed number and convert it to an integer
        current_num = int(label["text"])

        # Get the user input from the entry field and convert it to an integer
        input_value = int(entry.get())

        # Add or subtract based on the button clicked
        if is_addition:
            updated_num = current_num + input_value
        else:
            updated_num = current_num - input_value

        # Update the label with the new number
        label.config(text=str(updated_num))

    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid integer in both fields.")

# ==== GUI Setup ====

# Create the main window
window = tk.Tk()
window.title("Increment and Decrement Calculator")
window.geometry("400x200+600+300")
window.resizable(False, False)

# Label to show the current number (initialized to 0)
label = tk.Label(window, text="0", font=("Arial", 24))
label.place(relx=0.5, rely=0.2, anchor='center')

# Entry box for user to input the increment or decrement value
entry = tk.Entry(window)
entry.place(relx=0.5, rely=0.4, anchor='center', width=180)

# Plus button to increment by the input value
button_plus = tk.Button(window, text="Plus", command=lambda: update_number(True))
button_plus.place(relx=0.5, rely=0.6, anchor='e', width=150, height=30)

# Minus button to decrement by the input value
button_minus = tk.Button(window, text="Minus", command=lambda: update_number(False))
button_minus.place(relx=0.5, rely=0.6, anchor='w', width=150, height=30)

# Run the application
window.mainloop()
