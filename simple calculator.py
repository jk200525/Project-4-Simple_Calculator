import tkinter as tk

def click(btn_text):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + btn_text)

def clear():
    entry.delete(0, tk.END)
    history_label.config(text="")

def backspace():
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current[:-1])  # remove last character

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
        history_label.config(text=f"Last: {result}")
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")
        history_label.config(text="Error")

# Window setup
window = tk.Tk()
window.title("Calculator")
window.geometry("300x460")
window.resizable(False, False)

entry = tk.Entry(window, font=("Arial", 18), borderwidth=5, relief="ridge", justify='right')
entry.pack(fill="both", padx=10, pady=(10, 0), ipady=10)

# History label
history_label = tk.Label(window, font=("Arial", 12), fg="gray", anchor="e")
history_label.pack(fill="both", padx=10, pady=(2, 10))

# Button layout
btn_texts = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', '.', '=', '+']
]

frame = tk.Frame(window)
frame.pack()

for row in btn_texts:
    row_frame = tk.Frame(frame)
    row_frame.pack(expand=True, fill="both")
    for text in row:
        if text == '=':
            btn = tk.Button(row_frame, text=text, height=2, width=6, font=("Arial", 14),
                            command=calculate, bg="#4CAF50", fg="white")
        else:
            btn = tk.Button(row_frame, text=text, height=2, width=6, font=("Arial", 14),
                            command=lambda t=text: click(t))
        btn.pack(side="left", expand=True, fill="both")

# Extra control buttons
extra_frame = tk.Frame(window)
extra_frame.pack(fill="both", padx=10, pady=5)

clear_btn = tk.Button(extra_frame, text="Clear", font=("Arial", 14), bg="red", fg="white", command=clear)
clear_btn.pack(side="left", expand=True, fill="both", padx=(0, 5))

cut_btn = tk.Button(extra_frame, text="⌫", font=("Arial", 14), bg="#FFA500", fg="black", command=backspace)
cut_btn.pack(side="left", expand=True, fill="both", padx=(5, 0))

window.mainloop()
