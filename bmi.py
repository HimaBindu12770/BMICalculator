import tkinter as tk
from tkinter import messagebox


def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())
        if weight <= 0 or height <= 0:
            messagebox.showerror("Error", "Please enter valid positive numbers!")
            return
        bmi = weight / (height ** 2)
        bmi = round(bmi, 2)
        category = classify_bmi(bmi)
        result_label.config(text=f"BMI: {bmi}\nCategory: {category}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers!")


def classify_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"


# GUI Window
window = tk.Tk()
window.title("BMI Calculator")
window.geometry("300x250")
window.config(bg="lightblue")

title_label = tk.Label(window, text="BMI Calculator 🧑‍⚕️", font=("Arial", 16), bg="lightblue")
title_label.pack(pady=10)

weight_label = tk.Label(window, text="Enter Weight (kg):", bg="lightblue")
weight_label.pack()
weight_entry = tk.Entry(window)
weight_entry.pack()

height_label = tk.Label(window, text="Enter Height (m):", bg="lightblue")
height_label.pack()
height_entry = tk.Entry(window)
height_entry.pack()

calc_button = tk.Button(window, text="Calculate BMI", command=calculate_bmi, bg="#4CAF50", fg="white")
calc_button.pack(pady=10)

result_label = tk.Label(window, text="", font=("Arial", 12), bg="lightblue")
result_label.pack()

window.mainloop()

