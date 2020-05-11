"""GUI Calculator.

This calculator can perform addition, subtraction, multiplication, 
division, and more.

Example:
    Open the calculator interface.

        $ python calculator.py

"""


from functools import wraps
from tkinter import *
from tkinter import ttk


def num_btn(n):
    """Update value displayed on screen when a number is selected."""
    value = calc_display.get()
    if value != "0":
        value += str(n)
    else:
        value = str(n)
    return calc_display.set(value)


def zero_btn():
    """Call num_btn() with the corresponding button value."""
    return num_btn(0)


def one_btn():
    """Call num_btn() with the corresponding button value."""
    return num_btn(1)


def two_btn():
    """Call num_btn() with the corresponding button value."""
    return num_btn(2)


def three_btn():
    """Call num_btn() with the corresponding button value."""
    return num_btn(3)


def four_btn():
    """Call num_btn() with the corresponding button value."""
    return num_btn(4)


def five_btn():
    """Call num_btn() with the corresponding button value."""
    return num_btn(5)


def six_btn():
    """Call num_btn() with the corresponding button value."""
    return num_btn(6)


def seven_btn():
    """Call num_btn() with the corresponding button value."""
    return num_btn(7)


def eight_btn():
    """Call num_btn() with the corresponding button value."""
    return num_btn(8)


def nine_btn():
    """Call num_btn() with the corresponding button value."""
    return num_btn(9)


def clear_btn():
    """Reset value displayed on screen to zero."""
    return calc_display.set(0)


def value_updater(fn):
    """Decorator to update value displayed on screen."""
    @wraps(fn)
    def wrapper(*args, **kwargs):
        value = calc_display.get()
        new_val = fn(value)
        return calc_display.set(new_val)
    return wrapper


@value_updater
def decimal_btn(value):
    """Add a decimal point to current value."""
    if value.count(".") == 0:
        value += "."
    elif value.count(".") == 1 and value.count(" "):
        value += "."
    return value


@value_updater
def del_btn(value):
    """Delete the last character from current value."""
    if len(value) > 1:
        if value[-1] == " ":
            return value[0:-3]
        else:
            return value[0:-1]
    else:
        return 0


@value_updater
def neg_btn(value):
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


@value_updater
def reciprocal_btn(value):
    """Return the reciprocal of the current value."""
    try:
        x = float(value)
        if x != 0:
            return 1 / x
        else:
            return "UNDEFINED"
    except ValueError:
        return "ERROR"


@value_updater
def squared_btn(value):
    """Return the square of the current value."""
    try:
        x = float(value)
        return x ** 2
    except ValueError:
        return "ERROR"


@value_updater
def sqrt_btn(value):
    """Return the square root of the current value."""
    try:
        x = float(value)
        if x > 0:
            return x ** (1/2)
        else:
            return "ERROR"
    except ValueError:
        return "ERROR"


@value_updater
def percent_btn(value):
    """Convert the current value to a percentage in decimal form."""
    try:
        x = float(value)
        return x / 100
    except ValueError:
        return "ERROR"


def addition(num1, num2):
    """Return the value of num1 plus num2."""
    new_val = num1 + num2
    return calc_display.set(new_val)


def subtraction(num1, num2):
    """Return the value of num1 minus num2."""
    new_val = num1 - num2
    return calc_display.set(new_val)


def multiplication(num1, num2):
    """Return the value of num1 multiplied by num2."""
    new_val = num1 * num2
    return calc_display.set(new_val)


def division(num1, num2):
    """Return the value of num1 divided by num2."""
    if num2 != 0:
        new_val = num1 / num2
    else:
        new_val = "UNDEFINED"
    return calc_display.set(new_val)


def exponent(num1, num2):
    """Return the value of num1 to the power of num2."""
    new_val = num1 ** num2
    return calc_display.set(new_val)


def equation_checker(fn):
    """Decorator to determine the response to a function call."""
    @wraps(fn)
    def wrapper(*args, **kwargs):
        value = calc_display.get()
        if value.count(" "):
            return split_equation(value)
        else:
            return fn(value)
    return wrapper


@equation_checker
def add_btn(value):
    """Add a plus sign to the current value."""
    new_val = value + " + "
    return calc_display.set(new_val)


@equation_checker
def sub_btn(value):
    """Add a minus sign to the current value."""
    new_val = value + " - "
    return calc_display.set(new_val)


@equation_checker
def mult_btn(value):
    """Add a multiplication sign to the current value."""
    new_val = value + " x "
    return calc_display.set(new_val)


@equation_checker
def div_btn(value):
    """Add a division sign to the current value."""
    new_val = value + " / "
    return calc_display.set(new_val)


@equation_checker
def exp_btn(value):
    """Add an exponent symbol to the current value."""
    new_val = value + " ^ "
    return calc_display.set(new_val)


@equation_checker
def equal_btn(value):
    """Return the current value if math operation is not specified."""
    return calc_display.set(value)


math_operators = {
    "^": exponent,
    "x": multiplication,
    "/": division,
    "+": addition,
    "-": subtraction
}


def math_selector(num1, math_symbol, num2):
    """Call the function for the indicated math operation."""
    for key in math_operators.keys():
        if key == math_symbol:
            return math_operators[key](num1, num2)


def split_equation(value):
    """Split the equation into num1, the math operation, and num2."""
    val_list = value.split(" ")
    num1 = float(val_list[0])
    math_symbol = val_list[1]
    num2 = float(val_list[2])
    return math_selector(num1, math_symbol, num2)


"""Set up the window."""
root = Tk()
root.title("Calculator")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

"""Create the widgets and place them onscreen."""
calc_display = StringVar()
calc_display.set(0)

ttk.Label(mainframe, textvariable=calc_display).grid(
    columnspan=5, row=1, sticky=(E))

ttk.Button(mainframe, text="%", command=percent_btn).grid(
    column=1, row=2, sticky=(W, E))
ttk.Button(mainframe, text="x^y", command=exp_btn).grid(
    column=2, row=2, sticky=(W, E))
ttk.Button(mainframe, text="C", command=clear_btn).grid(
    column=3, row=2, sticky=(W, E))
ttk.Button(mainframe, text="DEL", command=del_btn).grid(
    column=4, row=2, sticky=(W, E))

ttk.Button(mainframe, text="1/x", command=reciprocal_btn).grid(
    column=1, row=3, sticky=(W, E))
ttk.Button(mainframe, text="x^2", command=squared_btn).grid(
    column=2, row=3, sticky=(W, E))
ttk.Button(mainframe, text="x^(1/2)", command=sqrt_btn).grid(
    column=3, row=3, sticky=(W, E))
ttk.Button(mainframe, text="/", command=div_btn).grid(
    column=4, row=3, sticky=(W, E))

ttk.Button(mainframe, text="7", command=seven_btn).grid(
    column=1, row=4, sticky=(W, E))
ttk.Button(mainframe, text="8", command=eight_btn).grid(
    column=2, row=4, sticky=(W, E))
ttk.Button(mainframe, text="9", command=nine_btn).grid(
    column=3, row=4, sticky=(W, E))
ttk.Button(mainframe, text="x", command=mult_btn).grid(
    column=4, row=4, sticky=(W, E))

ttk.Button(mainframe, text="4", command=four_btn).grid(
    column=1, row=5, sticky=(W, E))
ttk.Button(mainframe, text="5", command=five_btn).grid(
    column=2, row=5, sticky=(W, E))
ttk.Button(mainframe, text="6", command=six_btn).grid(
    column=3, row=5, sticky=(W, E))
ttk.Button(mainframe, text="-", command=sub_btn).grid(
    column=4, row=5, sticky=(W, E))

ttk.Button(mainframe, text="1", command=one_btn).grid(
    column=1, row=6, sticky=(W, E))
ttk.Button(mainframe, text="2", command=two_btn).grid(
    column=2, row=6, sticky=(W, E))
ttk.Button(mainframe, text="3", command=three_btn).grid(
    column=3, row=6, sticky=(W, E))
ttk.Button(mainframe, text="+", command=add_btn).grid(
    column=4, row=6, sticky=(W, E))

ttk.Button(mainframe, text="(-)", command=neg_btn).grid(
    column=1, row=7, sticky=(W, E))
ttk.Button(mainframe, text="0", command=zero_btn).grid(
    column=2, row=7, sticky=(W, E))
ttk.Button(mainframe, text=".", command=decimal_btn).grid(
    column=3, row=7, sticky=(W, E))
ttk.Button(mainframe, text="=", command=equal_btn).grid(
    column=4, row=7, sticky=(W, E))

"""Add padding around each widget."""
for child in mainframe.winfo_children():
    child.grid_configure(padx=1, pady=1)

"""Call the equal_btn function if the Return key is pressed."""
root.bind('<Return>', equal_btn)

"""Run the application."""
if __name__ == "__main__":
    root.mainloop()
