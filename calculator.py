from tkinter import *
from tkinter import ttk


def num_btn(n):
    try:
        value = calc_display.get()
        if value != "0":
            # new_val = value + str(n)
            # calc_display.set(new_val)
            value += str(n)
            # calc_display.set(value)
        else:
            value = str(n)
            # calc_display.set(n)
        calc_display.set(value)
    except ValueError:
        pass


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
    try:
        calc_display.set(0)
    except ValueError:
        pass


def value_updater(fn):
    def wrapper(*args, **kwargs):
        value = calc_display.get()
        new_val = fn(value)
        return calc_display.set(new_val)
    return wrapper


@value_updater
def decimal_btn(value):
    try:
        # value = calc_display.get()
        if value.count(".") == 0:
            # new_val = value + "."
            value += "."
            # calc_display.set(new_val)
            return value
        else:
            return value
    except ValueError:
        pass


@value_updater
def del_btn(value):
    try:
        # value = calc_display.get()
        if len(value) > 1:
            # new_val = value[0:-1]
            return value[0:-1]
            # calc_display.set(new_val)
        else:
            return 0
            # new_val = 0
            # calc_display.set(0)
        # calc_display.set(new_val)
        # return new_val
    except ValueError:
        pass


def neg_btn():
    try:
        value = calc_display.get()
        if value.count(" "):
            val_list = value.split()
            num1 = val_list[0]
            math_symbol = val_list[1]
            num2 = float(val_list[2])
            num2 *= -1
            new_val = num1 + " " + math_symbol + " " + str(num2)
            calc_display.set(new_val)
        elif float(value) != 0:
            new_val = float(value) * -1
            calc_display.set(new_val)
        else:
            calc_display.set(0)
    except ValueError:
        pass


def reciprocal_btn():
    try:
        value = float(calc_display.get())
        if value != 0:
            new_val = 1 / value
            calc_display.set(new_val)
        else:
            calc_display.set("UNDEFINED")
    except FloatingPointError:
        pass


def squared_btn():
    try:
        value = float(calc_display.get())
        new_val = value ** 2
        calc_display.set(new_val)
    except ArithmeticError:
        pass


def sqrt_btn():
    try:
        value = float(calc_display.get())
        if value > 0:
            new_val = value ** (1/2)
            calc_display.set(new_val)
        else:
            calc_display.set("ERROR")
    except ArithmeticError:
        pass


def percent_btn():
    try:
        value = float(calc_display.get())
        new_val = value / 100
        calc_display.set(new_val)
    except ValueError:
        pass


def addition(num1, num2):
    try:
        # value = calc_display.get()
        # val_list = value.split(" + ")
        # x = float(val_list[0])
        # y = float(val_list[1])
        # new_val = x + y
        new_val = num1 + num2
        calc_display.set(new_val)
    except ArithmeticError:
        pass


def subtraction(num1, num2):
    try:
        # value = calc_display.get()
        # val_list = value.split(" - ")
        # x = float(val_list[0])
        # y = float(val_list[1])
        # new_val = x - y
        new_val = num1 - num2
        calc_display.set(new_val)
    except ArithmeticError:
        pass


def multiplication(num1, num2):
    try:
        # value = calc_display.get()
        # val_list = value.split(" x ")
        # x = float(val_list[0])
        # y = float(val_list[1])
        # new_val = x * y
        new_val = num1 * num2
        calc_display.set(new_val)
    except ArithmeticError:
        pass


def division(num1, num2):
    try:
        # value = calc_display.get()
        # val_list = value.split(" / ")
        # x = float(val_list[0])
        # y = float(val_list[1])
        if num2 != 0:
            new_val = num1 / num2
            calc_display.set(new_val)
        else:
            calc_display.set("UNDEFINED")
    except ArithmeticError:
        pass


def exponent(num1, num2):
    try:
        # value = calc_display.get()
        # val_list = value.split(" ^ ")
        # x = float(val_list[0])
        # y = float(val_list[1])
        new_val = num1 ** num2
        calc_display.set(new_val)
    except ArithmeticError:
        pass


def equation_checker(fn):
    def wrapper(*args, **kwargs):
        value = calc_display.get()
        if value.count(" "):
            # return equal_btn()
            return split_equation(value)
        else:
            # return fn(*args, **kwargs)
            return fn(value)
    return wrapper


@equation_checker
def add_btn(value):
    try:
        # value = calc_display.get()
        # if value.count(" "):
        #     return equal_btn()
        # else:
        #     new_val = value + " + "
        #     calc_display.set(new_val)
        new_val = value + " + "
        calc_display.set(new_val)
    except ArithmeticError:
        pass


@equation_checker
def sub_btn(value):
    try:
        # value = calc_display.get()
        # if value.count(" "):
        #     return equal_btn()
        # else:
        #     new_val = value + " - "
        #     calc_display.set(new_val)
        new_val = value + " - "
        calc_display.set(new_val)
    except ArithmeticError:
        pass


@equation_checker
def mult_btn(value):
    try:
        # value = calc_display.get()
        # if value.count(" "):
        #     return equal_btn()
        # else:
        #     new_val = value + " x "
        #     calc_display.set(new_val)
        new_val = value + " x "
        calc_display.set(new_val)
    except ArithmeticError:
        pass


@equation_checker
def div_btn(value):
    try:
        # value = calc_display.get()
        # if value.count(" "):
        #     return equal_btn()
        # else:
        #     new_val = value + " / "
        #     calc_display.set(new_val)
        new_val = value + " / "
        calc_display.set(new_val)
    except ArithmeticError:
        pass


@equation_checker
def exp_btn(value):
    try:
        # value = calc_display.get()
        # if value.count(" "):
        #     return equal_btn()
        # else:
        #     new_val = value + " ^ "
        #     calc_display.set(new_val)
        new_val = value + " ^ "
        calc_display.set(new_val)
    except ArithmeticError:
        pass


@equation_checker
def equal_btn(value):
    try:
        pass
        # return split_equation(value)
        # value = calc_display.get()
        # if value.count(" ^ "):
        #     return exponent()
        # elif value.count(" x "):
        #     return multiplication()
        # elif value.count(" / "):
        #     return division()
        # elif value.count(" + "):
        #     return addition()
        # elif value.count(" - "):
        #     return subtraction()
        # else:
        #     pass
    except ValueError:
        pass


math_operators = {
    "^": exponent,
    "x": multiplication,
    "/": division,
    "+": addition,
    "-": subtraction
}


def math_selector(num1, math_symbol, num2):
    for operator in math_operators.keys():
        if math_symbol == operator:
            return math_operators[operator](num1, num2)
        else:
            pass


def split_equation(value):
    try:
        # value = calc_display.get()
        # if value.count(" "):
        #     val_list = value.split(" ")
        #     num1 = float(val_list[0])
        #     math_symbol = val_list[1]
        #     num2 = float(val_list[2])
        #     return math_selector(num1, math_symbol, num2)
        # else:
        #     pass
        val_list = value.split(" ")
        num1 = float(val_list[0])
        math_symbol = val_list[1]
        num2 = float(val_list[2])
        return math_selector(num1, math_symbol, num2)
    except ValueError:
        pass


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
ttk.Button(mainframe, text="^", command=exp_btn).grid(
    column=2, row=2, sticky=(W, E))
ttk.Button(mainframe, text="C", command=clear_btn).grid(
    column=3, row=2, sticky=(W, E))
ttk.Button(mainframe, text="DEL", command=del_btn).grid(
    column=4, row=2, sticky=(W, E))

ttk.Button(mainframe, text="1/x",
           command=reciprocal_btn).grid(column=1, row=3, sticky=(W, E))
ttk.Button(mainframe, text="x^2", command=squared_btn).grid(
    column=2, row=3, sticky=(W, E))
ttk.Button(mainframe, text="x^(1/2)",
           command=sqrt_btn).grid(column=3, row=3, sticky=(W, E))
ttk.Button(mainframe, text="/", command=div_btn).grid(column=4,
                                                      row=3, sticky=(W, E))

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
ttk.Button(mainframe, text="-", command=sub_btn).grid(column=4,
                                                      row=5, sticky=(W, E))

ttk.Button(mainframe, text="1", command=one_btn).grid(
    column=1, row=6, sticky=(W, E))
ttk.Button(mainframe, text="2", command=two_btn).grid(
    column=2, row=6, sticky=(W, E))
ttk.Button(mainframe, text="3", command=three_btn).grid(
    column=3, row=6, sticky=(W, E))
ttk.Button(mainframe, text="+", command=add_btn).grid(column=4,
                                                      row=6, sticky=(W, E))

ttk.Button(mainframe, text="(-)",
           command=neg_btn).grid(column=1, row=7, sticky=(W, E))
ttk.Button(mainframe, text="0", command=zero_btn).grid(
    column=2, row=7, sticky=(W, E))
ttk.Button(mainframe, text=".", command=decimal_btn).grid(
    column=3, row=7, sticky=(W, E))
ttk.Button(mainframe, text="=", command=equal_btn).grid(
    column=4, row=7, sticky=(W, E))

for child in mainframe.winfo_children():
    child.grid_configure(padx=1, pady=1)

root.mainloop()

"""
def zero_btn():
    try:
        value = str(calc_display.get())
        if value != "0":
            new_val = value + "0"
            calc_display.set(int(new_val))
        else:
            calc_display.set(int(0))
    except ValueError:
        pass


def one_btn():
    try:
        value = str(calc_display.get())
        if value != "0":
            new_val = value + "1"
            calc_display.set(int(new_val))
        else:
            calc_display.set(int(1))
    except ValueError:
        pass


def two_btn():
    try:
        value = str(calc_display.get())
        if value != "0":
            new_val = value + "2"
            calc_display.set(int(new_val))
        else:
            calc_display.set(int(2))
    except ValueError:
        pass


def three_btn():
    try:
        value = str(calc_display.get())
        if value != "0":
            new_val = value + "3"
            calc_display.set(int(new_val))
        else:
            calc_display.set(int(3))
    except ValueError:
        pass


def four_btn():
    try:
        value = str(calc_display.get())
        if value != "0":
            new_val = value + "4"
            calc_display.set(int(new_val))
        else:
            calc_display.set(int(4))
    except ValueError:
        pass


def five_btn():
    try:
        value = str(calc_display.get())
        if value != "0":
            new_val = value + "5"
            calc_display.set(int(new_val))
        else:
            calc_display.set(int(5))
    except ValueError:
        pass


def six_btn():
    try:
        value = str(calc_display.get())
        if value != "0":
            new_val = value + "6"
            calc_display.set(int(new_val))
        else:
            calc_display.set(int(6))
    except ValueError:
        pass


def seven_btn():
    try:
        value = str(calc_display.get())
        if value != "0":
            new_val = value + "7"
            calc_display.set(int(new_val))
        else:
            calc_display.set(int(7))
    except ValueError:
        pass


def eight_btn():
    try:
        value = str(calc_display.get())
        if value != "0":
            new_val = value + "8"
            calc_display.set(int(new_val))
        else:
            calc_display.set(int(8))
    except ValueError:
        pass


def nine_btn():
    try:
        value = calc_display.get()
        if value != "0":
            new_val = value + "9"
            calc_display.set(new_val)
        else:
            calc_display.set(9)
    except ValueError:
        pass
"""

"""
def calculate(*args):
    try:
        value = float(feet.get())
        meters.set((0.3048 * value * 10000.0 + 0.5)/10000.0)
    except ValueError:
        pass


feet = StringVar()
meters = StringVar()

feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet)
feet_entry.grid(column=2, row=1, sticky=(W, E))

ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E))
ttk.Button(mainframe, text="Calculate", command=calculate).grid(
    column=3, row=3, sticky=W)

ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)

for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

feet_entry.focus()
root.bind('<Return>', calculate)
"""
