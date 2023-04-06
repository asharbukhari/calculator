from gui import CalculatorGUI as cg
from function import Arithmetic_operation as ao
import tkinter as tk

cal = cg(tk.Tk())
func = ao(cal)

cal.add_button['command'] = func.addition
cal.divide_button['command'] = func.division
cal.subtract_button['command'] = func.subtraction
cal.multiply_button['command'] = func.multipication

cal.master.mainloop()






