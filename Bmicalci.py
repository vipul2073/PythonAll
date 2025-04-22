import tkinter as tk
from tkinter import messagebox

def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get()) / 100  # convert cm to meters
        bmi = round(weight / (height ** 2), 2)

        if bmi < 18.5:
            category = "Underweight"
        elif 18.5 <= bmi < 24.9:
            category = "Normal weight"
        elif 25 <= bmi < 29.9:
            category = "Overweight"
        else:
            category = "Obese"

        result_label.config(text=f"BMI: {bmi} ({category})")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")

# GUI setup
root = tk.Tk()
root.title("BMI Calculator")

tk.Label(root, text="Weight (kg):").grid(row=0, column=0, padx=10, pady=5)
weight_entry = tk.Entry(root)
weight_entry.grid(row=0, column=1, pady=5)

tk.Label(root, text="Height (cm):").grid(row=1, column=0, padx=10, pady=5)
height_entry = tk.Entry(root)
height_entry.grid(row=1, column=1, pady=5)

tk.Button(root, text="Calculate BMI", command=calculate_bmi).grid(row=2, column=0, columnspan=2, pady=10)

result_label = tk.Label(root, text="Enter your details to calculate BMI")
result_label.grid(row=3, column=0, columnspan=2, pady=5)

root.mainloop()

