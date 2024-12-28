import tkinter as tk
from tkinter import messagebox

# Function to handle button clicks
def button_click(value):
    entry.insert(tk.END, value)

# Function to evaluate the expression
def calculate():
    result = eval(entry.get())  # Evaluate the expression
    entry.delete(0, tk.END)
    entry.insert(0, str(result))
    # try:
    #     result = eval(entry.get())  # Evaluate the expression
    #     entry.delete(0, tk.END)
    #     entry.insert(0, str(result))
    # except ZeroDivisionError:
    #     messagebox.showerror("Error", "Cannot divide by zero!")
    # except Exception:
    #     messagebox.showerror("Error", "Invalid input!")

# Function to clear the entry field
def clear():
    entry.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Entry widget for display
entry = tk.Entry(root, font=("Arial", 16), justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Button layout
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('C', 4, 0), ('0', 4, 1), ('=', 4, 2), ('+', 4, 3),
]

# Add buttons to the window
for text, row, col in buttons:
    if text == "=":
        btn = tk.Button(root, text=text, width=5, height=2, command=calculate)
    elif text == "C":
        btn = tk.Button(root, text=text, width=5, height=2, command=clear)
    else:
        btn = tk.Button(root, text=text, width=5, height=2, command=lambda val=text: button_click(val))
    btn.grid(row=row, column=col, padx=5, pady=5)

# Run the application
root.mainloop()
