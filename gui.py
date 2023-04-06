import tkinter as tk
class CalculatorGUI:
    def __init__(self, master):
        super.__init__
        self.master = master
        master.title("Calculator")

        self.label1 = tk.Label(master, text="Enter First Number:")
        self.label1.pack()

        self.num1_entry = tk.Entry(master)
        self.num1_entry.pack()

        self.label2 = tk.Label(master, text="Enter Second Number:")
        self.label2.pack()

        self.num2_entry = tk.Entry(master)
        self.num2_entry.pack()

        self.add_button = tk.Button(master, text="+")
        self.add_button.pack(side=tk.LEFT, padx=5)

        self.subtract_button = tk.Button(master, text="-")
        self.subtract_button.pack(side=tk.LEFT, padx=5)

        self.multiply_button = tk.Button(master, text="x")
        self.multiply_button.pack(side=tk.LEFT, padx=5)

        self.divide_button = tk.Button(master, text="/")
        self.divide_button.pack(side=tk.LEFT, padx=5)

        self.result_label = tk.Label(master, text="Result:")
        self.result_label.pack()

        self.result_text = tk.Label(master)
        self.result_text.pack()

        master.geometry("300x150")
    

