"""Alternate #1: GUI Calculator.

This calculator can perform addition, subtraction, multiplication, 
division, and more.

Example:
    Open the calculator interface.

        $ python calculator-oop.py

"""


from tkinter import *
from tkinter import ttk


class Calculator(Tk):

    def __init__(self):
        super().__init__()

        """Set up the window."""
        self.title("Calculator")

        self.mainframe = ttk.Frame(self, padding=(12, 12, 12, 12))
        self.mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        """First row."""
        self.calc_display = StringVar()
        self.calc_display.set(0)

        self.calc_screen = ttk.Label(
            self.mainframe,
            textvariable=self.calc_display
        )
        self.calc_screen.grid(columnspan=5, row=0, sticky=(E))

        """Second row."""
        self.btn_percent = ttk.Button(
            self.mainframe,
            text="%",
            command=lambda: self.value_updater(self.percentage)
        )
        self.btn_percent.grid(column=1, row=1, sticky=(W, E))

        self.btn_exponent = ttk.Button(
            self.mainframe,
            text="x^y",
            command=lambda: self.equation_checker(" ^ ")
        )
        self.btn_exponent.grid(column=2, row=1, sticky=(W, E))

        self.btn_clear = ttk.Button(
            self.mainframe,
            text="C",
            command=lambda: self.calc_display.set(0)
        )
        self.btn_clear.grid(column=3, row=1, sticky=(W, E))

        self.btn_delete = ttk.Button(
            self.mainframe,
            text="DEL",
            command=lambda: self.value_updater(self.delete)
        )
        self.btn_delete.grid(column=4, row=1, sticky=(W, E))

        """Third row."""
        self.btn_reciprocal = ttk.Button(
            self.mainframe,
            text="1/x",
            command=lambda: self.value_updater(self.reciprocal)
        )
        self.btn_reciprocal.grid(column=1, row=2, sticky=(W, E))

        self.btn_square = ttk.Button(
            self.mainframe,
            text="x^2",
            command=lambda: self.value_updater(self.square)
        )
        self.btn_square.grid(column=2, row=2, sticky=(W, E))

        self.btn_squareroot = ttk.Button(
            self.mainframe,
            text="x^(1/2)",
            command=lambda: self.value_updater(self.squareroot)
        )
        self.btn_squareroot.grid(column=3, row=2, sticky=(W, E))

        self.btn_divide = ttk.Button(
            self.mainframe,
            text="/",
            command=lambda: self.equation_checker(" / ")
        )
        self.btn_divide.grid(column=4, row=2, sticky=(W, E))

        """Fourth row."""
        self.btn_seven = ttk.Button(
            self.mainframe,
            text="7",
            command=lambda: self.num_btn(7)
        )
        self.btn_seven.grid(column=1, row=3, sticky=(W, E))

        self.btn_eight = ttk.Button(
            self.mainframe,
            text="8",
            command=lambda: self.num_btn(8)
        )
        self.btn_eight.grid(column=2, row=3, sticky=(W, E))

        self.btn_nine = ttk.Button(
            self.mainframe,
            text="9",
            command=lambda: self.num_btn(9)
        )
        self.btn_nine.grid(column=3, row=3, sticky=(W, E))

        self.btn_multiply = ttk.Button(
            self.mainframe,
            text="x",
            command=lambda: self.equation_checker(" x ")
        )
        self.btn_multiply.grid(column=4, row=3, sticky=(W, E))

        """Fifth row."""
        self.btn_four = ttk.Button(
            self.mainframe,
            text="4",
            command=lambda: self.num_btn(4)
        )
        self.btn_four.grid(column=1, row=4, sticky=(W, E))

        self.btn_five = ttk.Button(
            self.mainframe,
            text="5",
            command=lambda: self.num_btn(5)
        )
        self.btn_five.grid(column=2, row=4, sticky=(W, E))

        self.btn_six = ttk.Button(
            self.mainframe,
            text="6",
            command=lambda: self.num_btn(6)
        )
        self.btn_six.grid(column=3, row=4, sticky=(W, E))

        self.btn_subtract = ttk.Button(
            self.mainframe,
            text="-",
            command=lambda: self.equation_checker(" - ")
        )
        self.btn_subtract.grid(column=4, row=4, sticky=(W, E))

        """Sixth row."""
        self.btn_one = ttk.Button(
            self.mainframe,
            text="1",
            command=lambda: self.num_btn(1)
        )
        self.btn_one.grid(column=1, row=5, sticky=(W, E))

        self.btn_two = ttk.Button(
            self.mainframe,
            text="2",
            command=lambda: self.num_btn(2)
        )
        self.btn_two.grid(column=2, row=5, sticky=(W, E))

        self.btn_three = ttk.Button(
            self.mainframe,
            text="3",
            command=lambda: self.num_btn(3)
        )
        self.btn_three.grid(column=3, row=5, sticky=(W, E))

        self.btn_add = ttk.Button(
            self.mainframe,
            text="+",
            command=lambda: self.equation_checker(" + ")
        )
        self.btn_add.grid(column=4, row=5, sticky=(W, E))

        """Seventh row."""
        self.btn_negative = ttk.Button(
            self.mainframe,
            text="(-)",
            command=lambda: self.value_updater(self.negative)
        )
        self.btn_negative.grid(column=1, row=6, sticky=(W, E))

        self.btn_zero = ttk.Button(
            self.mainframe,
            text="0",
            command=lambda: self.num_btn(0)
        )
        self.btn_zero.grid(column=2, row=6, sticky=(W, E))

        self.btn_decimal = ttk.Button(
            self.mainframe,
            text=".",
            command=lambda: self.value_updater(self.decimal)
        )
        self.btn_decimal.grid(column=3, row=6, sticky=(W, E))

        self.btn_equal = ttk.Button(
            self.mainframe,
            text="=",
            command=lambda: self.equation_checker("")
        )
        self.btn_equal.grid(column=4, row=6, sticky=(W, E))

        """Add padding around widgets."""
        for child in self.mainframe.winfo_children():
            child.grid_configure(padx=1, pady=1)

        """Call the equal_btn function if the Return key is pressed."""
        self.bind('<Return>', self.btn_equal["command"])

    def num_btn(self, n):
        """Update current value when a number button is selected."""
        value = self.calc_display.get()
        if value != "0":
            value += str(n)
        else:
            value = str(n)
        return self.calc_display.set(value)

    def value_updater(self, fn):
        """Update value displayed on screen."""
        value = self.calc_display.get()
        new_val = fn(value)
        return self.calc_display.set(new_val)

    def decimal(self, value):
        """Add a decimal point to current value."""
        if value.count(".") == 0:
            value += "."
        elif value.count(".") == 1 and value.count(" "):
            value += "."
        return value

    def delete(self, value):
        """Delete the last character from current value."""
        if len(value) > 1:
            if value[-1] == " ":
                return value[0:-3]
            else:
                return value[0:-1]
        else:
            return 0

    def negative(self, value):
        """Return the current value multiplied by -1."""
        if value.count(" "):
            val_list = value.split()
            num1 = val_list[0]
            math_symbol = val_list[1]
            num2 = float(val_list[2]) * -1
            num2 = str(num2)
            return f"{num1} {math_symbol} {num2}"
        elif float(value) != 0:
            return float(value) * -1
        else:
            return 0

    def reciprocal(self, value):
        """Return the reciprocal of the current value."""
        try:
            x = float(value)
            if x != 0:
                return 1 / x
            else:
                return "UNDEFINED"
        except ValueError:
            return "ERROR"

    def square(self, value):
        """Return the square of the current value."""
        try:
            x = float(value)
            return x ** 2
        except ValueError:
            return "ERROR"

    def squareroot(self, value):
        """Return the square root of the current value."""
        try:
            x = float(value)
            if x > 0:
                return x ** (1/2)
            else:
                return "ERROR"
        except ValueError:
            return "ERROR"

    def percentage(self, value):
        """Convert the current value to a percentage in decimal form."""
        try:
            x = float(value)
            return x / 100
        except ValueError:
            return "ERROR"

    def addition(self, num1, num2):
        """Return the value of num1 plus num2."""
        return num1 + num2

    def subtraction(self, num1, num2):
        """Return the value of num1 minus num2."""
        return num1 - num2

    def multiplication(self, num1, num2):
        """Return the value of num1 multiplied by num2."""
        return num1 * num2

    def division(self, num1, num2):
        """Return the value of num1 divided by num2."""
        if num2 != 0:
            return num1 / num2
        else:
            return "UNDEFINED"

    def exponent(self, num1, num2):
        """Return the value of num1 to the power of num2."""
        return num1 ** num2

    def equation_checker(self, operator):
        """Determine the response to a function call."""
        math_operators = {
            "^": self.exponent,
            "x": self.multiplication,
            "/": self.division,
            "+": self.addition,
            "-": self.subtraction
        }
        value = self.calc_display.get()
        if value.count(" "):
            val_list = value.split(" ")
            num1 = float(val_list[0])
            math_symbol = val_list[1]
            num2 = float(val_list[2])
            new_val = math_operators[math_symbol](num1, num2)
        else:
            new_val = value + operator
        return self.calc_display.set(new_val)


if __name__ == "__main__":
    calculator = Calculator()
    calculator.mainloop()
