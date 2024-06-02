import tkinter as tk



MAIN_ROW = 7
MAIN_COLUMN = 4
DIGITS = {
    7: (3,0), 8: (3,1), 9: (3,2),
    4: (4,0), 5: (4,1), 6: (4,2),
    1: (5,0), 2: (5,1), 3: (5,2),
    "00":(6,0), 0: (6,1), ".": (6,2)
}
OTHERS = {
    "C": (2,0),
    "%": (2,1),
    "<": (2,2),
}
OPERATORS = {
    "/": "\u00f7", "*": "\u00D7", "-": "-", "+": "+","=":"=",
}




class Calculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("375x667")
        self.window.title("Calculator")
        self.window.resizable(0,0)
        self.window.iconbitmap("./icon.ico")

        # row and column config
        self.window.rowconfigure(list(range(MAIN_ROW)), weight=1, uniform="a")
        self.window.columnconfigure(list(range(MAIN_COLUMN)), weight=1, uniform="a")

        # expression and result data
        self.expression_data = tk.StringVar(value="")
        self.result_data = tk.StringVar(value="0")
        # expression and result labels
        self.display_expression_label = self.create_display_label(0,0,"SE",("Helvetica", 20), self.expression_data)
        self.display_result_label = self.create_display_label(0,1,"E",("Helvetica", 30), self.result_data)

        self.create_digit_buttons = self.create_digit_buttons()
        self.create_operator_buttons = self.create_operator_buttons()
        self.create_other_buttons()
        self.full_operation = []
        self.display_nums = []

    def update_result(self, digit):
        # self.whole_digit +=  digit
        # self.result_data.set(self.whole_digit)
        self.display_nums.append(str(digit))
        full_number = "".join(self.display_nums)
        self.result_data.set(full_number)

    def update_expression_lebel(self):
        pass

    def math_operator(self, value):
        current_number = "".join(self.display_nums)
        if current_number:
            self.full_operation.append(current_number)

            if value != "=":
                self.full_operation.append(value)
                self.display_nums.clear()
                
                self.result_data.set("")
                self.expression_data.set(" ".join(self.full_operation))
            else:
                expression = "".join(self.full_operation)
                result = eval(expression)

                if isinstance(result, float):
                    if result.is_integer():
                        result = int(result)
                    else:
                        result = round(result, 3)

                self.full_operation.clear()
                self.display_nums = [str(result)]

                self.result_data.set(result)
                self.expression_data.set(expression)
    
    def other_button(self, value):
        if value == "C":
            self.result_data.set("0")
            self.expression_data.set("")

            self.display_nums.clear()
            self.full_operation.clear()
        elif value == "%":
            if self.display_nums:
                current_number = float("".join(self.display_nums))
                percentage = current_number/100

                self.display_nums = list(str(percentage))
                self.result_data.set("".join(self.display_nums))
        elif value == "<":
            if self.display_nums:
                self.display_nums.pop()
                self.result_data.set("".join(self.display_nums))


    def create_operator_buttons(self):
        i = 2
        for operator, symbol in OPERATORS.items():
            button = tk.Button(self.window, text=symbol,borderwidth=0,bg="orange",font=("Helvetica",20), command=lambda x=operator: self.math_operator(x))
            button.grid(column=3,row=i, sticky="NSEW")
            i+=1

    def create_digit_buttons(self):
        for digit, grid_val in DIGITS.items():
            button = tk.Button(self.window, text=str(digit), font=("Helvetica",20),bg="white",borderwidth=0, command=lambda x=digit: self.update_result(str(x)))
            button.grid(column=grid_val[1],row=grid_val[0],sticky="NSEW")
    
    def create_other_buttons(self):
        for operator, grid_val in OTHERS.items():
            button = tk.Button(self.window, text=str(operator),borderwidth=0,bg="orange",font=("Helvetica",20), command=lambda x=operator: self.other_button(x))
            button.grid(column=grid_val[1], row=grid_val[0],sticky="NSEW")

    
    def create_display_label(self,col,row, anchor,font,string_value):
        expression_label = tk.Label(self.window, text="0", font=font,padx=10, textvariable=string_value)
        expression_label.grid(column=col,columnspan=4,row=row, sticky=anchor)

    def run(self):
        self.window.mainloop()
        
if __name__ == "__main__":
    calculator = Calculator()
    calculator.run()