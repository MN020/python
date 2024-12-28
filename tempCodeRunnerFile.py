import tkinter as tk

def on_button_click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + value)

def on_calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Create main window
window = tk.Tk()
window.title("Calculator")

# Entry widget for displaying expressions
entry = tk.Entry(window, width=16, font=('Arial', 24), borderwidth=2, relief='solid')
entry.grid(row=0, column=0, columnspan=4)

# Button definitions
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3)
]

# Adding buttons to the grid
for (text, row, col) in buttons:
    button = tk.Button(window, text=text, width=10, height=3, 
                       command=lambda t=text: on_button_click(t) if t != '=' else on_calculate())
    button.grid(row=row, column=col)

# Run the main event loop
window.mainloop()