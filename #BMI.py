import tkinter as tk
from tkinter import messagebox

def calculate_bmi():

        weight = float(entry_weight.get())
        height = float(entry_height.get()) / 100
        bmi = weight / (height ** 2)
        label_result.config(text=bmi)
        if bmi < 18.5:
            messagebox.showinfo("Result", "Underweight")
        elif 18.5 <= bmi < 24.9:
            messagebox.showinfo("Result", "Normal weight")
        elif 25 <= bmi < 29.9:
            messagebox.showinfo("Result", "Overweight")
        elif not weight.isdigit() or not height.isdigit():
            messagebox.showerror("Erorr", "Please Enter Correct Value!")
        else:
            messagebox.showinfo("Result", "Obesity")
        

# Create the main window
root = tk.Tk()
root.title("BMI Calculator")
root.geometry("300x200")
root.configure(bg="#f0f0f0")

# Weight label and entry
label_weight = tk.Label(root, text="Weight (kg):", bg="#f0f0f0")
label_weight.pack(pady=5)
entry_weight = tk.Entry(root)
entry_weight.pack(pady=5)

# Height label and entry
label_height = tk.Label(root, text="Height (cm):", bg="#f0f0f0")
label_height.pack(pady=5)
entry_height = tk.Entry(root)
entry_height.pack(pady=5)

# Calculate button
button_calculate = tk.Button(root, text="Calculate", command=calculate_bmi, bg="#4CAF50", fg="white")
button_calculate.pack(pady=10)

# Result label
label_result = tk.Label(root, text="", bg="#f0f0f0")
label_result.pack(pady=5)

# Run the main loop
root.mainloop()
