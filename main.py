from definitions import calc
import tkinter as tk
from functools import partial

test_values = [
    ("32\"", "1440"),
    ("55 inch", "1080p"),
    ("110\"", "4k"),
    ("110ft", "QXGA"),
    ("30 foot 8.5\"", "4k")
]
button_identities = []

diagonal_values = (
    '19\"',
    '24\"',
    '32\"',
    '43\"',
    '55\"',
    '65\"',
    '7\'',
    '8\'',
    '9\''
)
resolution_values = (
    "720",
    "WXGA",
    "1080",
    "1440",
    "4k"
)
bg_color = "black"
fg_color = "hot pink"

class MyButton(tk.Button):

    def __init__(self, *args, **kwargs):
        tk.Button.__init__(self, *args, **kwargs)
        self['bg'] = bg_color
        self['fg'] = fg_color
        self['bd'] = 3


class MyFrame(tk.Frame):

    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        self['bg'] = bg_color


class MyLabel(tk.Label):

    def __init__(self, *args, **kwargs):
        tk.Label.__init__(self, *args, **kwargs)
        self['bg'] = bg_color
        self['fg'] = fg_color


class MyEntry(tk.Entry):

    def __init__(self, *args, **kwargs):
        tk.Entry.__init__(self, *args, **kwargs)
        self['bg'] = bg_color
        self['fg'] = fg_color
        self['bd'] = 1


def clear_frame(x):
    for widget in x.winfo_children():
        widget.destroy()


def clear_default(event):
    event.widget.delete(0, "end")
    return None


def change(v, target):
    target.delete(0, 'end')
    target.insert(0, v)


def propose_values(v, target, target_frame):
    frame = MyFrame(master=target_frame)
    for i, item in enumerate(v):
        button = MyButton(master=frame, text=item, command=partial(change, item, target))
        button.pack(side="left")
        button_identities.append(button)
    frame.grid(row=1, column=1)


def print_results(l):
    for item in l:
        label = MyLabel(master=output_frame, text=item, borderwidth=3, foreground="teal", width=390)
        string = item
        label.config(text=string)
        label.pack(side="bottom", pady=5)


def return_pressed(event):
    d = diagonal_entry.get()
    s = resolution_entry.get()
    result = f'{d}, {s}'
    for x in calc(d, s):
        result = result + f'\n{x}'
    print(len(results))
    results.insert(0, result)
    while len(results) > 3:
        results.pop(3)
    clear_frame(output_frame)
    print_results(results)


window = tk.Tk()
window.configure(bg="black")
window.geometry("400x400")
window.title("AV Calculator")
window.columnconfigure(0, weight=1)
window.rowconfigure(0, weight=1)
window.rowconfigure(1, weight=0)


input_frame = MyFrame(master=window)
picker_frame = MyFrame(master=input_frame)
diagonal_frame = MyFrame(master=picker_frame)
resolution_frame = MyFrame(master=picker_frame)
output_frame = MyFrame()

input_frame.columnconfigure(0, weight=1)
input_frame.columnconfigure(1, weight=0)
picker_frame.columnconfigure(0, weight=1)

diagonal_label = MyLabel(master=diagonal_frame, text="Diagonal Size Class", padx=10)
diagonal_label.grid(row=0, column=1)
diagonal_entry = MyEntry(diagonal_frame, justify='center')
diagonal_entry.insert(0, "<custom>")

diagonal_entry.grid(row=1, column=0, sticky='ew', padx=10)

propose_values(diagonal_values, diagonal_entry, diagonal_frame)
diagonal_frame.grid(row=0, sticky='ew')
diagonal_frame.grid_columnconfigure(0, weight=1)

dimension_label = MyLabel(master=resolution_frame, text="Resolution Class", padx=10)
dimension_label.grid(row=0, column=1)
resolution_entry = MyEntry(resolution_frame, justify='center')
resolution_entry.insert(0, "<custom>")
resolution_entry.grid(row=1, column=0, sticky='ew', padx=10)
propose_values(resolution_values, resolution_entry, resolution_frame)
resolution_frame.grid(row=1, sticky='ew')
resolution_frame.grid_columnconfigure(0, weight=1)

execute_button = MyButton(master=input_frame, text='=', width=3)
execute_button.grid(row=0, column=1, padx=10, pady=3, sticky='nsew')
picker_frame.grid(row=0, column=0, sticky='ew')

results = []

output_frame.grid(row=0, sticky="ew", padx=3)
input_frame.grid(row=1, pady=10, sticky='ew')

diagonal_entry.bind("<Button-1>", clear_default)
resolution_entry.bind("<Button-1>", clear_default)
execute_button.bind("<Button-1>", return_pressed)
window.bind("<Return>", return_pressed)
window.bind("<Backspace>", clear_frame(output_frame))
window.mainloop()

# d_prompt = "Enter display diagonal measurement\n"
# d = input(d_prompt.upper())
# r_prompt = "Enter display resolution\n"
# s = input(r_prompt.upper())

# calc(d, s)
# print(messages.my_messages)
"""for d, s in test_values:
    print(d, s)
    calc(d, s)
    print(messages.my_messages)
    messages.my_messages.clear()
"""
