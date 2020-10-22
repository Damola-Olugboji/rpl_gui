import tkinter as tk
from tkinter import ttk
from sys import argv

x = 0
n = 0
inc = 0


class entry_nounit(tk.Frame):
    def __init__(self, parent, text):
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
            "Stagnation Temperature(K): ": "28",
            "Stagnation Pressure(MPa): ": "35",
            "Throat Radius(M): ": "96",
            "Real Wall Temperature(K): ": "37",
            "Gamma: " : "159",
            "Specific Heat of Exhaust: ": "50",
            "W value: ": "160",
            "Characteristic Velocity(m/s): ": "27",
            "Recovery Factor: ":"109"
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
        # self.p.configure(bg="#222831", fg="white")
        # self.p["menu"].config(bg="red")


    def val(self):
        if self.entry.get() == "":
            return "nan"
        return float(self.entry.get())
    def default(self,text):
        self.entry.insert(0, text)
    def clear(self):
        self.entry.delete(0, 'end')

