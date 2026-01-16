# main.py
import tkinter as tk
from calc_backend import evaluate

# Create main window
root = tk.Tk()
root.title("Scientific Calculator")
root.geometry("400x500")

# Entry box for typing
entry = tk.Entry(root, font=("Arial", 20), borderwidth=4, relief="ridge")
entry.pack(pady=20, fill="x", padx=10)

def on_button_click(value):
    entry.insert(tk.END, value)

def clear_entry():
    entry.delete(0, tk.END)

def calculate():
    expr = entry.get()
    result = evaluate(expr)
    entry.delete(0, tk.END)
    entry.insert(0, result)

frame = tk.Frame(root)
frame.pack()

buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', '.', '=', '+'],
    ['sin', 'cos', 'tan', 'sqrt'],
    ['log', 'pi', '(', ')'],
    ['C']
]

for row in buttons:
    row_frame = tk.Frame(frame)
    row_frame.pack(expand=True, fill='both')
    for btn_text in row:
        if btn_text == '=':
            action = calculate
        elif btn_text == 'C':
            action = clear_entry
        else:
            action = lambda t=btn_text: on_button_click(t)
        tk.Button(row_frame, text=btn_text, font=("Arial", 14),
                  command=action, height=2, width=6).pack(side='left', expand=True, fill='both')

root.mainloop()