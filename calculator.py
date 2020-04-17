# Project: GUI Calculator
# This calculator can perform addition, subtraction, multiplication, division, and more.
# Terminal Input: python3 calculator.py

from tkinter import *
from tkinter import ttk


def num_btn(n):
    value = calc_display.get()
    if value != "0":
        value += str(n)
    else:
        value = str(n)
    return calc_display.set(value)


def zero_btn():
    return num_btn(0)


def one_btn():
    return num_btn(1)


def two_btn():
    return num_btn(2)


def three_btn():
    return num_btn(3)


def four_btn():
    return num_btn(4)


def five_btn():
    return num_btn(5)


def six_btn():
    return num_btn(6)


def seven_btn():
    return num_btn(7)


def eight_btn():
    return num_btn(8)


def nine_btn():
    return num_btn(9)


def clear_btn():
    return calc_display.set(0)


def value_updater(fn):
    def wrapper(*args, **kwargs):
        value = calc_display.get()
        new_val = fn(value)
        return calc_display.set(new_val)
    return wrapper


@value_updater
def decimal_btn(value):
    if value.count(".") == 0:
        value += "."
    elif value.count(".") == 1 and value.count(" "):
        value += "."
    return value


@value_updater
def del_btn(value):
    if len(value) > 1:
        if value[-1] == " ":
            return value[0:-3]
        else:
            return value[0:-1]
    else:
        return 0


@value_updater
def neg_btn(value):
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
    try:
        x = float(value)
        return x ** 2
    except ValueError:
        return "ERROR"


@value_updater
def sqrt_btn(value):
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
    try:
        x = float(value)
        return x / 100
    except ValueError:
        return "ERROR"


def addition(num1, num2):
    new_val = num1 + num2
    return calc_display.set(new_val)


def subtraction(num1, num2):
    new_val = num1 - num2
    return calc_display.set(new_val)


def multiplication(num1, num2):
    new_val = num1 * num2
    return calc_display.set(new_val)


def division(num1, num2):
    if num2 != 0:
        new_val = num1 / num2
    else:
        new_val = "UNDEFINED"
    return calc_display.set(new_val)


def exponent(num1, num2):
    new_val = num1 ** num2
    return calc_display.set(new_val)


def equation_checker(fn):
    def wrapper(*args, **kwargs):
        value = calc_display.get()
        if value.count(" "):
            return split_equation(value)
        else:
            return fn(value)
    return wrapper


@equation_checker
def add_btn(value):
    new_val = value + " + "
    return calc_display.set(new_val)


@equation_checker
def sub_btn(value):
    new_val = value + " - "
    return calc_display.set(new_val)


@equation_checker
def mult_btn(value):
    new_val = value + " x "
    return calc_display.set(new_val)


@equation_checker
def div_btn(value):
    new_val = value + " / "
    return calc_display.set(new_val)


@equation_checker
def exp_btn(value):
    new_val = value + " ^ "
    return calc_display.set(new_val)


@equation_checker
def equal_btn(value):
    return calc_display.set(value)


math_operators = {
    "^": exponent,
    "x": multiplication,
    "/": division,
    "+": addition,
    "-": subtraction
}


def math_selector(num1, math_symbol, num2):
    for key in math_operators.keys():
        if key == math_symbol:
            return math_operators[key](num1, num2)


def split_equation(value):
    val_list = value.split(" ")
    num1 = float(val_list[0])
    math_symbol = val_list[1]
    num2 = float(val_list[2])
    return math_selector(num1, math_symbol, num2)


root = Tk()
root.title("Calculator")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

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

for child in mainframe.winfo_children():
    child.grid_configure(padx=1, pady=1)

root.bind('<Return>', equal_btn)

root.mainloop()
