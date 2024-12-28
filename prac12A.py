import tkinter as tk

def submit_input():
    name = entry.get()
    label_result.config(text=f"Hello, {name}!")

# Create the main window
window = tk.Tk()
window.title("Simple GUI")

# Create widgets
label = tk.Label(window, text="Enter your name:")
entry = tk.Entry(window)
button = tk.Button(window, text="Submit", command=submit_input)
label_result = tk.Label(window, text="")

# Layout the widgets
label.pack()
entry.pack()
button.pack()
label_result.pack()

# Run the GUI
window.mainloop()
