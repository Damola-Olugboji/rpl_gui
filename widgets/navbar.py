import tkinter as tk


class navbar(tk.Frame):
    def __init__(self, parent, controller, page_name):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.controller = controller
        self.page_name = page_name
        self.configure(bg="#222831")
        self.nav_items(controller, page_name)

    def nav_items(self, controller, page_name):
        self.page_name = page_name
        button1 = tk.Button(
            self,
            text="Propellant",
            font=("Garamond", 18),
            width=10,
            height=1,
            command=lambda: self.controller.show_frame("propellant"),
            bg="white",
            relief="raised",
            borderwidth="10",
            highlightbackground="red",
        )
        button2 = tk.Button(
            self,
            text="Engine",
            command=lambda: self.controller.show_frame("engine"),
            font=("Garamond", 18),
            width=10,
            height=1,
            bg="white",
            borderwidth="10",
        )
        button3 = tk.Button(
            self,
            text="Contour ",
            command=lambda: self.controller.show_frame("nozzle"),
            font=("Garamond", 18),
            width=10,
            height=1,
            bg="white",
            borderwidth="10",
        )
        button4 = tk.Button(
            self,
            text="Heat Transfer",
            command=lambda: self.controller.show_frame("heat"),
            font=("Garamond", 18),
            width=10,
            height=1,
            bg="white",
            borderwidth="10",
        )
        exitButton = tk.Button(
            self,
            text="Exit",
            font=("Garamond", 18),
            fg="white",
            bg="#ff5260",
            width=10,
            height=0,
            command=exit,
            borderwidth="10",
        )
        button1.grid(column=0, row=0, pady=15, padx=10)
        button2.grid(column=1, row=0, pady=15, padx=10)
        button3.grid(column=2, row=0, pady=15, padx=10)
        button4.grid(column=3, row=0, pady=15, padx=10)
        exitButton.grid(column=4, row=0, pady=10, padx=45)

        if page_name == "propellant":
            button1.configure(bg="#3282b8", fg="white")
            button2.configure(bg="#ffffff")
            button3.configure(bg="#ffffff")
            button4.configure(bg="#ffffff")
        if page_name == "engine":
            button1.configure(bg="#ffffff")
            button2.configure(bg="#3282b8", fg="white")
            button3.configure(bg="#ffffff")
            button4.configure(bg="#ffffff")
        if page_name == "nozzle":
            button1.configure(bg="#ffffff")
            button2.configure(bg="#ffffff")
            button3.configure(bg="#3282b8", fg="white")
            button4.configure(bg="#ffffff")
        if page_name == "heat":
            button1.configure(bg="#ffffff")
            button2.configure(bg="#ffffff")
            button3.configure(bg="#ffffff")
            button4.configure(bg="#3282b8", fg="white")
