import tkinter as tk
from tkinter import messagebox

def calculate_flames_result(name1, name2):
    name1 = name1.lower().replace(" ", "")
    name2 = name2.lower().replace(" ", "")
    
    for char in name1:
        if char in name2:
            name1 = name1.replace(char, "", 1)
            name2 = name2.replace(char, "", 1)

    total_chars = len(name1) + len(name2)
    flames = "FLAMES"
    relationship = flames[total_chars % len(flames) - 1]
    return relationship

def show_result():
    name1 = entry_name1.get()
    name2 = entry_name2.get()

    if name1 and name2:
        result = calculate_flames_result(name1, name2)
        relationship = get_relationship(result)
        messagebox.showinfo("Result", f"The relationship between {name1} and {name2} is: {relationship}")
    else:
        messagebox.showwarning("Warning", "Please enter both names.")

def get_relationship(result):
    relationships = {
        "F": "Friends",
        "L": "Lovers",
        "A": "Affectionate",
        "M": "Marriage",
        "E": "Enemies",
        "S": "Siblings"
    }
    return relationships.get(result, "Unknown")

# Create the main window
root = tk.Tk()
root.title("FLAMES Game")

# Labels and Entry fields
label_name1 = tk.Label(root, text="Enter your name:")
label_name1.grid(row=0, column=0)

entry_name1 = tk.Entry(root)
entry_name1.grid(row=0, column=1)

label_name2 = tk.Label(root, text="Enter the other person's name:")
label_name2.grid(row=1, column=0)

entry_name2 = tk.Entry(root)
entry_name2.grid(row=1, column=1)

# Calculate button
btn_calculate = tk.Button(root, text="Calculate", command=show_result)
btn_calculate.grid(row=2, columnspan=2)

# Run the main loop
root.mainloop()
