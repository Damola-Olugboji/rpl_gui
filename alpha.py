import tkinter as tk
from widgets.navbar import navbar
from pages.engine import engine_calculations
from calculations.tree_results import tree
from pages.propellant import propellant_calculations


def exit():
    app.quit()


def sendInformation(p1):
    pass


class GUI(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (engine, nozzle, heat, propellant):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            frame.configure(bg="#222831")

            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("propellant")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()


class engine(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.parent = parent
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        # self.grid_rowconfigure(0, weight=1)
        # self.grid_rowconfigure(2, weight=1)
        self.navbar = navbar(self, controller, "engine")
        self.navbar.grid(column=0, row=0, columnspan=10, sticky="n")
        label = tk.Label(
            self,
            text="Engine Analysis",
            font=("Garamond", 25),
            fg="white",
            bg="#222831",
        )
        label.grid(pady=(20, 10), row=1, columnspan=2, sticky="w", padx=80)
        calcs = engine_calculations(self)
        calcs.grid(column=0, row=2, columnspan=10, padx=80, sticky="w")
        # add warning to use one unit for pressure calculations


class nozzle(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.controller = controller
        self.navbar = navbar(self, controller, "nozzle")
        self.navbar.grid(column=0, row=0, columnspan=10, sticky="n")

        label = tk.Label(
            self,
            text="Nozzle Characteristics",
            font=("Garamond", 25),
            fg="white",
            bg="#222831",
        )
        label.grid(pady=10)


class heat(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.controller = controller
        self.navbar = navbar(self, controller, "heat")
        self.navbar.grid(column=0, row=0, columnspan=10, sticky="n")

        label = tk.Label(
            self,
            text="Thermodynamic Analysis",
            font=("Garamond", 25),
            fg="white",
            bg="#222831",
        )
        label.grid(pady=10)


class propellant(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.parent = parent
        self.controller = controller
        self.navbar = navbar(self, controller, "propellant")
        self.navbar.grid(column=0, row=0, columnspan=10, sticky="n")

        label = tk.Label(
            self,
            text="Propellant Properties / Chamber Performance",
            font=("Garamond", 25),
            fg="white",
            bg="#222831",
        )
        label.grid(pady=(20, 10), row=1, columnspan=2, sticky="w", padx=80)
        self.prop = propellant_calculations(self)
        self.prop.grid(column=0, row=2, sticky="w", padx=80)


if __name__ == "__main__":
    app = GUI()
    app.geometry("1100x630+30+30")
    app.minsize(1100, 630)
    app.maxsize(1100, 630)
    app.mainloop()
"""
chamber pressure
chamber temperature
solid product chamber density
propellant specific heat ratio (gamma)
combustion efficiency
"""
