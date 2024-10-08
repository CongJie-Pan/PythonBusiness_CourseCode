import tkinter as tk
from tkinter import messagebox

def show_greeting():
    name = entry_name.get()
    age = entry_age.get()

    # Validate that the name contains only alphabetic (字母) characters
    if not name.isalpha():
        greeting_label.config(text="Name should only contain alphanumeric characters")
        return

    # Validate that the age is a number
    if not age.isdigit():
        greeting_label.config(text="Age should only contain digits")

    # Convert age to an integer after validation
    age = int(age)
    greeting_label.config(text=f"Hello {name}, You are {age} years old.")


# Create the main window
window = tk.Tk()
window.title("Simple Greeting Application")

# Set the window size and disable resizing
window.geometry("400x300+600+300")
window.resizable(False, False)

# Create and place a label
label = tk.Label(window, text="Enter your name:")
label.pack(pady = 10)

# Create a label for displaying the greeting, initially empty
greeting_label = tk.Label(window, text="")
greeting_label.pack(pady = 10)

# Create and place an entry (input box)
entry_name = tk.Entry(window)
entry_name.pack(pady = 5)

# Create and place an entry(input box) for the age
entry_age = tk.Entry(window)
entry_age.pack(pady = 5)

# Create and place a button
button = tk.Button(window, text="Greet", command=show_greeting)
button.pack(pady = 10)

# Create an Exit button that closes the window
exit_button = tk.Button(window, text="Exit", command=window.destroy)
exit_button.pack(pady = 5)

# Run the application
window.mainloop()