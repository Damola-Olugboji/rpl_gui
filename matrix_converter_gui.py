import tkinter as tk
from tkinter import filedialog
import pandas as pd
import numpy as np
import csv
import sys
import os
import time

root = tk.Tk()
root.title("RRPL Matrix Converter")
root.geometry("300x150")


def UploadAction(event=None):
    filename = filedialog.askopenfilename()
    print("Selected:", filename)
    if str(filename)[-1] == "x" or str(filename)[-1] == "v":
        entry(filename)
    else:
        time.sleep(2)
        sys.exit()


button = tk.Button(root, text="Import File", command=UploadAction, width="20")
button.place(relx=0.5, rely=0.3, anchor="center")
output = tk.Label(root, text="incorrect format will cause the program to exit")
output.place(relx=0.1, rely=0.6)


def entry(file):
    if str(file[-1]) == "v":
        df = pd.read_csv(file, header=None)
        df = np.array(df)
        solidworks(df)
    else:
        df = pd.read_excel(file, header=None)
        df = np.array(df)
        solidworks(df)


def solidworks(df):
    results = []
    for i in range(0, len(df)):
        for c in range(0, len(df[i])):
            results.append(df[i][c])

    results = [results[i : i + 2] for i in range(0, len(results), 2)]
    for i in range(0, len(results)):
        results[i] = [x for x in results[i] if str(x) != "nan"]

    with open("Coordinates_solid_works.csv", "w", newline="") as myfile:
        for i in range(0, len(results) - 1):
            wr = csv.writer(myfile)
            wr.writerow(results[i])

    df1 = pd.read_csv("Coordinates_solid_works.csv", header=None)
    df1.insert(2, "0", 0)
    df1.to_csv("Coordinates_solid_works.csv", mode="w", index=False, header=None)

    ansys("Coordinates_solid_works.csv", results)


def ansys(filename, results):
    with open("Coordinates_ansys.csv", "w", newline="") as myfile:
        wr = csv.writer(myfile)
        item1, item2 = ["polyline=true"], ["3d=true"]
        wr.writerow(item1)
        wr.writerow(item2)
        for i in range(0, len(results) - 2):
            if -1 in results[i]:
                continue
            results[i].insert(0, 0)
            wr.writerow(results[i])

    output.config(text="COMPLETED", fg="red")


root.mainloop()
