import tkinter as tk
from tkinter import ttk


class tree(tk.Frame):
    def __init__(self, parent, outputs):
        tk.Frame.__init__(self, parent)
        self.outputs = outputs
        self.style = ttk.Style(self)
        self.style.configure("Treeview", bg="#222831", fg="white")
        self.treev = ttk.Treeview(
            self, columns=("", "values", "Units"), selectmode="browse"
        )
        self.treev["column"] = ("0", "1", "2")
        self.treev["show"] = "headings"
        self.treev.heading("0", text="Names")
        self.treev.heading("1", text="Values")
        self.treev.heading("2", text="Units")

        self.treev.column("0", width=200, stretch=tk.YES)
        self.treev.column("1", width=90, stretch=tk.YES)
        self.treev.column("2", width=70, stretch=tk.YES)
        self.treev.pack(side="left")
        self.scrollbar = ttk.Scrollbar(
            self, orient="vertical", command=self.treev.yview
        )
        self.scrollbar.pack(side="right", fill="y", expand=tk.FALSE)
        self.treev.configure(yscrollcommand=self.scrollbar.set)
        for i in range(0, len(outputs)):
            self.treev.insert(
                parent="",
                index="end",
                values=(self.outputs[i][0], self.outputs[i][1], self.outputs[i][2]),
            )
        self.style = ttk.Style(self)
        self.style.theme_use("clam")
        self.style.configure(
            "Treeview",
            background="#222831",
            fieldbackground="#222831",
            foreground="white",
        )

        # self.treev.configure(font=("Times New Roman", 10))

