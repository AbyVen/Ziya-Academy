import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        root.title("Simple Calculator")
        self.expression = ""
        self.input_text = tk.StringVar()

        self.input_frame = tk.Frame(root, bd=2, relief=tk.RIDGE)
        self.input_frame.pack(side=tk.TOP)

        self.input_field = tk.Entry(self.input_frame, font=('arial', 18), textvariable=self.input_text, width=30, bd=5, relief=tk.RIDGE, justify='right')
        self.input_field.grid(row=0, column=0)
        self.input_field.pack(ipady=10)

        self.button_frame = tk.Frame(root)
        self.button_frame.pack()

        buttons = [
            ['C', '<', '%', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['+/-', '0', '.', '=']
        ]

        for r, row in enumerate(buttons):
            for c, btn_text in enumerate(row):
                btn = tk.Button(self.button_frame, text=btn_text, width=6, height=2, font=('arial', 16),
                                bd=1, relief=tk.RIDGE,
                                command=lambda b=btn_text: self.button_click(b))
                btn.grid(row=r, column=c, padx=1, pady=1)

    def button_click(self, char):
        if char == "C":
            self.expression = ""
        elif char == "<":
            self.expression = self.expression[:-1]
        elif char == "=":
            try:
                self.expression = str(eval(self.expression))
            except Exception:
                self.expression = "Error"
        elif char == "+/-":
            try:
                if self.expression:
                    if self.expression.startswith('-'):
                        self.expression = self.expression[1:]
                    else:
                        self.expression = '-' + self.expression
            except:
                self.expression = "Error"
        else:
            self.expression += str(char)
        self.input_text.set(self.expression)

if __name__ == "__main__":
    root = tk.Tk()
    calc = Calculator(root)
    root.mainloop()
