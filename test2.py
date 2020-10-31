import tkinter as tk
from tkinter import filedialog
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

root = tk.Tk()
rStar = 0.0765
k = 1.214
exitMach = 3.21
cm = (k - 1) / 2
cp = (k + 1) / 2
cpm = (k + 1) / (2 * (k - 1))


def bartz():
    filename = filedialog.askopenfilename()
    df = pd.read_csv(filename, header=None)
    df = np.array(df)
    formatdf = np.array2string(df, formatter={"float_kind": lambda x: "%.7f" % x})
    height = len(df)
    # print(df)
    stepSize = 0.00005
    maxIteration = 20000
    convCond = 0.0005
    lastMach = 1
    for i in range(0, height):
        converged = False
        r = df[i][1]
        rRatioTarget = (r / rStar) ** 2
        currentIteration = 1
        M = lastMach

        while converged == False and currentIteration < maxIteration and low <= high:
            testCase = (1 / M) * ((1 + cm * (M ** 2) / cp) ** cpm)
            # print(str(currentIteration) + ": " + str(M))
            if abs(testCase - rRatioTarget) <= convCond:
                converged = True
                lastMach = M
            else:
                currentIteration += 1
                M = M + stepSize
        if converged == False:
            pass
            # print("error")
        print(M)


def bartzb():
    filename = filedialog.askopenfilename()
    df = pd.read_csv(filename, header=None)

    df = np.array(df)
    formatdf = np.array2string(
        df,
    )
    # print(round(df[6][1]))
    height = len(df)
    # print(df)
    # print(height)
    stepSize = 0.00005
    maxIteration = 20000
    convCond = 0.0001
    lastMach = 1
    # print(df)
    machArray = []
    rArray = []
    for i in range(0, height):

        converged = False
        r = round(df[i][1], 7)
        firstR = round(df[0][1], 7)
        rRatioTarget = (r / rStar) ** 2
        currentIteration = 1
        # print(rRatioTarget)
        low = 1
        high = exitMach + 0.5
        counter = 0
        print(
            "------------------------------------Index [ "
            + str(i)
            + " ]--------------------------------------"
        )
        # print("r = " + str(r))
        while converged == False and low <= high:

            mid = (low + high) / 2
            # print("high: " + str(high) + " | mid: " + str(mid) + " | low: " + str(low))
            M = mid
            testCase = (1 / M) * (
                (1 + cm * (M ** 2) / cp) ** cpm
            )  # if left side > right side mach increases

            if round(df[i][1], 7) == firstR:
                converged = True
                M = 1.0
            elif abs(testCase - rRatioTarget) <= convCond:
                converged = True
            else:
                # print(M)
                if testCase < rRatioTarget:
                    low = mid + stepSize
                elif testCase > rRatioTarget:
                    high = mid - stepSize

            # print(str(counter) + ": " + str(M))
            counter += 1
            # print(counter)
            # print("low: " + str(low) + "  Mid: " + str(mid) + " high: " + str(high))
            """print(
                "DF Value: "
                + str(round(df[i][1], 7))
                + "    |   Index: "
                + str(i)
                + "  |   Test Case: "
                + str(round(testCase, 10))
                + "  |   Mach: "
                + str(mid)
            )
            print(
                "Target: "
                + str(rRatioTarget)
                + " | testCase: "
                + str(testCase)
                + " | Converge: "
                + str(abs(testCase - rRatioTarget))
            )"""

        # print("Mach: " + str(round(M, 9)))
        machArray.append(M)
        rArray.append(r)
        if converged == False:
            pass
            # print("error")
    # plt.plot(machArray, rArray)
    plt.xlabel("Mach")
    plt.ylabel("Nozzle")
    plt.scatter(machArray, rArray)
    plt.show()


button = tk.Button(root, text="Import", command=bartzb).pack()


root.geometry("200x200")
root.mainloop()