import tkinter as tk
from tkinter import filedialog
import matplotlib
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def plot_frame(title, xmax, ymax, data, text):
    matplotlib.use("TkAgg")

    top = tk.Toplevel()
    top.title(title)
    figure = Figure(figsize=(5, 4), dpi=100)
    plot = figure.add_subplot(1, 1, 1)
    # plot.plot(self.visc_gas_mix_a[-1], 3500, color="blue", marker="o", linestyle="")
    x = [*range(1, xmax + 1, 1)]
    y = data
    plot.plot(x, y, color="red", linestyle=":")

    canvas = FigureCanvasTkAgg(figure, top)
    canvas.get_tk_widget().grid(row=0, column=0)

    label = tk.Label(
        top,
        text=text,
        anchor="e",
    )
    label.grid(row=1, column=0)

    figure = Figure(figsize=(5, 4), dpi=100)
