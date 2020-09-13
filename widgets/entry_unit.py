import tkinter as tk
from tkinter import ttk
from sys import argv

x = 0
n = 0
inc = 0


class entry_with_unit(tk.Frame):
    def __init__(self, parent, text, value):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.text = text
        self.configure(bg="#222831")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.name = tk.Label(
            self,
            text=text,
            font=("Franklin Gothic Medium", 12),
            fg="white",
            bg="#222831",
        )
        padding = {
            "Chamber Pressure: ": "28",
            "Chamber Temperature: ": "0",
            "Ambient Pressure: ": "33",
            "Thrust Desired: ": "57",
            "Gamma: ": "99",
            "Total Impulse: ": "62"
        }
        if not (text in padding):
            self.pad = 20
        else:
            self.pad = padding[text]

        self.name.pack(side="left", fill="x", expand=True)
        self.entry = tk.Entry(self, width=10, font = ("Franklin Gothic Medium", 12))
        self.entry.pack(side="left", padx=(self.pad, 15))
        # self.rowconfigure(0, weight=1)
        # self.columnconfigure(0, weight=1)
        self.n = tk.StringVar()
        self.value = value
        self.p = tk.OptionMenu(self, self.n, *value)
        self.p.configure(cursor="hand2")
        # self.p.configure(bg="#222831", fg="white")
        self.n.set(value[0])
        # self.p["menu"].config(bg="red")
        self.p.pack(side="left")

    def unit(self):
        return self.n.get()

    def val(self):
        if self.entry.get() == "":
            return "nan"
        return float(self.entry.get())
    def default(self,text):
        self.entry.insert(0, text)
    def clear(self):
        self.entry.delete(0, 'end')

"""
gamma 100 , 7
thrust desried 55, 16
nozzle exit pressure 20, 22
chamber temperature 0, 21
Chamber Pressure 28, 18
"""
