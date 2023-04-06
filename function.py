
class Arithmetic_operation:
    
    def __init__(self,master):
        self.master = master
        
        
    def addition(self):
        x = self.master.num1_entry.get()
        y = self.master.num2_entry.get()
        self.master.result_text["text"] = int(x) + int(y)
        
    def subtraction(self):
        x = self.master.num1_entry.get()
        y = self.master.num2_entry.get()
        self.master.result_text["text"] = int(x) - int(y)

    def multipication(self):
        x = self.master.num1_entry.get()
        y = self.master.num2_entry.get()
        self.master.result_text["text"] = int(x) * int(y)

    def division(self):
        x = self.master.num1_entry.get()
        y = self.master.num2_entry.get()
        self.master.result_text["text"] = int(x) / int(y)

        