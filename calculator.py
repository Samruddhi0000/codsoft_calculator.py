import tkinter as tk

def on_click(text):
    current = expression.get()
    if text == "AC":
        expression.set("")
    elif text == "=":
        try:
            result = str(eval(current.replace("×", "*").replace("÷", "/").replace("−", "-")))
            expression.set(result)
        except:
            expression.set("Error")
    elif text == "+/−":
        if current.startswith("-"):
            expression.set(current[1:])
        else:
            expression.set("-" + current)
    else:
        expression.set(current + text)

# Main Window
root = tk.Tk()
root.title("Calculator")
root.configure(bg="black")
root.resizable(False, False)

# Display
expression = tk.StringVar()
expression.set("")
display = tk.Label(root, textvariable=expression, anchor="e", bg="black", fg="white",
                   font=("Helvetica", 36), padx=20, pady=30)
display.grid(row=0, column=0, columnspan=4, sticky="we")

# Button layout
buttons = [
    ["AC", "+/−", "%", "÷"],
    ["7", "8", "9", "×"],
    ["4", "5", "6", "−"],
    ["1", "2", "3", "+"],
    ["0", ".", "=", ""]
]

# Button color mapper
def get_color(text):
    if text in ["AC", "+/−", "%"]:
        return "#a5a5a5"  # Light gray
    elif text in ["÷", "×", "−", "+", "="]:
        return "#ff9500"  # Orange
    else:
        return "#333333"  # Dark gray

# Create buttons
for r, row in enumerate(buttons, start=1):
    c = 0
    while c < 4:
        char = row[c]
        if char == "":
            c += 1
            continue

        colspan = 2 if char == "0" else 1

        btn = tk.Button(
            root, text=char, font=("Helvetica", 22),
            fg="white", bg=get_color(char), activebackground="#888",
            bd=0, width=5 if char != "0" else 11, height=2,
            command=lambda ch=char: on_click(ch)
        )
        btn.grid(row=r, column=c, columnspan=colspan, padx=5, pady=5, sticky="we")

        c += colspan

# Equal column/row weights
for i in range(4):
    root.grid_columnconfigure(i, weight=1)
for i in range(1, 6):
    root.grid_rowconfigure(i, weight=1)

# Run the app
root.mainloop()
