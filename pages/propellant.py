import tkinter as tk
import pypropep as ppp
from tkinter import ttk
import os, sys, math
from data.propellant_data import propellant_data
from widgets.autoComboBox import AutocompleteCombobox

"""
Thermodynamic Performance and Chemical Equilibrium Composition Calculations
based on Nasa publication by Sanford Gordon and Bonnie J. McBride
https://www.grc.nasa.gov/www/CEAWeb/RP-1311.pdf
"""


class propellant_calculations(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.configure(bg="#222831")
        # self.frame = tk.Frame(self)
        ppp.init()
        # self.frame.grid(column=0, row=0, sticky="nesw")
        self.label = tk.Label(
            self,
            text="Propellant Names",
            fg="white",
            bg="#222831",
            font=("Garamond", 15),
        )
        self.label.grid(column=0, row=0)
        w, h = 2, 12
        self.weight_label = tk.Label(
            self, text="Weight(gr)", fg="white", bg="#222831", font=("Garamond", 15)
        )
        self.weight_label.grid(column=1, row=0)
        self.prop = [[0 for x in range(w)] for y in range(h)]
        for i in range(0, h):
            self.prop[i][0] = AutocompleteCombobox(self)
            self.prop[i][0].set_completion_list(propellant_data)
            self.prop[i][0].configure(width="40", font=("Franklin Gothic Medium", 12))
            self.prop[i][0].grid(column=0, row=i + 1, pady=3)
            self.prop[0][0].focus_set()
            self.prop[i][1] = tk.Entry(
                self, width=10, font=("Franklin Gothic Medium", 10)
            )
            self.prop[i][1].grid(column=1, row=i + 1, padx=(10, 0))
