import tkinter as tk
from tkinter import messagebox
from datetime import date

def calculate_age():
    try:
        birth_year = int(entry_birth_year.get())
        birth_month = int(entry_birth_month.get())
        birth_day = int(entry_birth_day.get())

        today = date.today()
        current_year = today.year
        current_month = today.month
        current_day = today.day

        age = current_year - birth_year - ((current_month, current_day) < (birth_month, birth_day))

        messagebox.showinfo("Age Calculator", f"Your age is {age} years.")
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter valid numbers for birth year, month, and day.")

# Create the main window
root = tk.Tk()
root.title("Age Calculator")

# Labels
label_birth_date = tk.Label(root, text="Enter your birthdate:")
label_birth_date.pack()

# Entry fields
entry_birth_year = tk.Entry(root, width=4)
entry_birth_year.insert(0, "YYYY")
entry_birth_year.pack(side=tk.LEFT)

label_year = tk.Label(root, text="Year")
label_year.pack(side=tk.LEFT)

entry_birth_month = tk.Entry(root, width=2)
entry_birth_month.insert(0, "MM")
entry_birth_month.pack(side=tk.LEFT)

label_month = tk.Label(root, text="Month")
label_month.pack(side=tk.LEFT)

entry_birth_day = tk.Entry(root, width=2)
entry_birth_day.insert(0, "DD")
entry_birth_day.pack(side=tk.LEFT)

label_day = tk.Label(root, text="Day")
label_day.pack(side=tk.LEFT)

# Calculate button
btn_calculate = tk.Button(root, text="Calculate Age", command=calculate_age)
btn_calculate.pack()

# Run the main loop
root.mainloop()
