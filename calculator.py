from tkinter import *
from tkinter import ttk


def num_btn(n):
    try:
        value = calc_display.get()
        if value != "0":
            new_val = value + str(n)
            calc_display.set(new_val)
        else:
            calc_display.set(n)
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


def decimal_btn():
    try:
        value = calc_display.get()
        if value.count(".") == 0:
            new_val = value + "."
            calc_display.set(new_val)
        else:
            pass
    except ValueError:
        pass


def clear_btn():
    try:
        calc_display.set(0)
    except ValueError:
        pass


def del_btn():
    try:
        value = calc_display.get()
        if len(value) > 1:
            new_val = value[0:-1]
            calc_display.set(new_val)
        else:
            calc_display.set(0)
    except ValueError:
        pass


def neg_btn():
    try:
        value = int(calc_display.get())
        if value != 0:
            new_val = value * -1
            calc_display.set(new_val)
        else:
            calc_display.set(0)
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


ttk.Button(mainframe, text="%").grid(column=1, row=2, sticky=(W, E))
ttk.Button(mainframe, text="^").grid(column=2, row=2, sticky=(W, E))
ttk.Button(mainframe, text="C", command=clear_btn).grid(
    column=3, row=2, sticky=(W, E))
ttk.Button(mainframe, text="DEL", command=del_btn).grid(
    column=4, row=2, sticky=(W, E))

ttk.Button(mainframe, text="1/x").grid(column=1, row=3, sticky=(W, E))
ttk.Button(mainframe, text="x^2").grid(column=2, row=3, sticky=(W, E))
ttk.Button(mainframe, text="x^(1/2)").grid(column=3,
                                           row=3, sticky=(W, E))
ttk.Button(mainframe, text="/").grid(column=4, row=3, sticky=(W, E))

ttk.Button(mainframe, text="7", command=seven_btn).grid(
    column=1, row=4, sticky=(W, E))
ttk.Button(mainframe, text="8", command=eight_btn).grid(
    column=2, row=4, sticky=(W, E))
ttk.Button(mainframe, text="9", command=nine_btn).grid(
    column=3, row=4, sticky=(W, E))
ttk.Button(mainframe, text="x").grid(column=4, row=4, sticky=(W, E))

ttk.Button(mainframe, text="4", command=four_btn).grid(
    column=1, row=5, sticky=(W, E))
ttk.Button(mainframe, text="5", command=five_btn).grid(
    column=2, row=5, sticky=(W, E))
ttk.Button(mainframe, text="6", command=six_btn).grid(
    column=3, row=5, sticky=(W, E))
ttk.Button(mainframe, text="-").grid(column=4, row=5, sticky=(W, E))

ttk.Button(mainframe, text="1", command=one_btn).grid(
    column=1, row=6, sticky=(W, E))
ttk.Button(mainframe, text="2", command=two_btn).grid(
    column=2, row=6, sticky=(W, E))
ttk.Button(mainframe, text="3", command=three_btn).grid(
    column=3, row=6, sticky=(W, E))
ttk.Button(mainframe, text="+").grid(column=4, row=6, sticky=(W, E))

ttk.Button(mainframe, text="(-)",
           command=neg_btn).grid(column=1, row=7, sticky=(W, E))
ttk.Button(mainframe, text="0", command=zero_btn).grid(
    column=2, row=7, sticky=(W, E))
ttk.Button(mainframe, text=".", command=decimal_btn).grid(
    column=3, row=7, sticky=(W, E))
ttk.Button(mainframe, text="=").grid(column=4, row=7, sticky=(W, E))

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
