import tkinter as tk

def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def division(a, b):
    if b == 0:
        return "Error"
    return a / b

def multiplication(a, b):
    return a * b

first_number = 0
operator = ""

def press(x):
    entry.insert("end", x)

def choose_operation(op):
    global first_number, operator
    first_number = float(entry.get())
    operator = op
    entry.delete(0, "end")

def equals():
    second_number = float(entry.get())

    if operator == "+":
        answer = addition(first_number, second_number)
    elif operator == "-":
        answer = subtraction(first_number, second_number)
    elif operator == "*":
        answer = multiplication(first_number, second_number)
    elif operator == "/":
        answer = division(first_number, second_number)

    entry.delete(0, "end")
    entry.insert(0, answer)

def clear():
    entry.delete(0, "end")

root = tk.Tk()
root.title("Calculator")
root.geometry("320x420")
root.resizable(False, False)

entry = tk.Entry(
    root,
    font=("Arial", 28),
    justify="right"
)

entry.pack(
    fill="x",
    padx=10,
    pady=10,
    ipady=10
)

button_frame = tk.Frame(root)
button_frame.pack(expand=True, fill="both", padx=10, pady=10)

buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["C", "0", "=", "+"]
]

for r in range(4):
    for c in range(4):
        x = buttons[r][c]

        if x in "0123456789":
            cmd = lambda x=x: press(x)
        elif x in "+-*/":
            cmd = lambda x=x: choose_operation(x)
        elif x == "=":
            cmd = equals
        else:
            cmd = clear

        tk.Button(
            button_frame,
            text=x,
            font=("Arial", 20),
            command=cmd
        ).grid(
            row=r,
            column=c,
            sticky="nsew",
            padx=2,
            pady=2
        )

for i in range(4):
    button_frame.rowconfigure(i, weight=1)
    button_frame.columnconfigure(i, weight=1)

root.mainloop()