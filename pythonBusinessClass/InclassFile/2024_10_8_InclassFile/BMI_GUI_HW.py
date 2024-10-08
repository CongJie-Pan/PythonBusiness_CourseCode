import tkinter as tk
from tkinter import messagebox

def show_BMI_Result():
    weight = entry_weight.get()
    height = entry_height.get()

    # Validate that weight and height are numbers
    if not weight.isdigit() or not height.isdigit():
        infoShow_label.config(text="Weight and height should only contain digits.")
        return

    # Convert weight and height to integers after validation
    weight = int(weight)
    height = int(height)

    # Calculating the BMI Result
    BMI_Value = weight / ((height / 100) ** 2)
    BMI_Value = round(BMI_Value, 2)  # Round the result to 2 decimal places

    # Determine the category based on the BMI value
    if BMI_Value < 18.5:
        infoShow_label.config(text=f"Your BMI is {BMI_Value}, You are in Thinness.")
    elif BMI_Value < 24:
        infoShow_label.config(text=f"Your BMI is {BMI_Value}, You are in Normal.")
    elif BMI_Value <= 35:
        infoShow_label.config(text=f"Your BMI is {BMI_Value}, You are in Overweight.")
    else:
        infoShow_label.config(text=f"Your BMI is {BMI_Value}, You are in Obesity.")

# Create the main window
window = tk.Tk()
window.title("BMI Calculator")

# Set the window size and disable resizing
window.geometry("400x300+600+300")
window.resizable(False, False)

# Create and place a "Enter your weight(kg)" label on the left
label_weight = tk.Label(window, text="Enter your weight (kg):")
label_weight.place(x=20, y=30)

# Create and place an entry(input box) for the weight on the right
entry_weight = tk.Entry(window)
entry_weight.place(x=180, y=30, width=180)

# Create and place a "Enter your height(cm)" label on the left
label_height = tk.Label(window, text="Enter your height (cm):")
label_height.place(x=20, y=70)

# Create and place an entry(input box) for the height on the right
entry_height = tk.Entry(window)
entry_height.place(x=180, y=70, width=180)

# Create a button for calculating BMI and place it
button_calculate = tk.Button(window, text="BMI Calculate", command=show_BMI_Result)
button_calculate.place(x=220, y=110, width=100, height=30)

# Create a label for displaying the BMI result, initially empty, and place it at the bottom
infoShow_label = tk.Label(window, text="", fg="blue")
infoShow_label.place(x=20, y=160, width=360)

# Create an Exit button that closes the window and place it
exit_button = tk.Button(window, text="Exit", command=window.destroy)
exit_button.place(x=160, y=220, width=70, height=30)

# Run the application
window.mainloop()
