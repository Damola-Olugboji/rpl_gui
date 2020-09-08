import tkinter as tk


class checkbox(tk.Frame):
    def __init__(self, parent, text):
        tk.Frame.__init__(self, parent)
        self.configure(bg="#222831")
        self.parent = parent
        self.text = text
        self.var = tk.BooleanVar()
        self.var.set(False)
        self.check = tk.Checkbutton(self, variable=self.var, text=self.text)
        self.check.pack()
        self.check.configure(
            bg="#222831", fg="white", font=("Franklin Gothic Medium", 12)
        )

    def val(self):
        return self.var

