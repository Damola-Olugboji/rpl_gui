import tkinter as tk
from tkinter import filedialog
from widgets.entry_nounit import entry_nounit as enu
import math, csv
import pandas as pd
import numpy as np
import matplotlib
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class heatTransferHub(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.configure(bg="#222831")
        self.toggle1 = tk.Button(
            self,
            text="Bartz Heat ",
            font=("Garamond", 15),
            command=lambda *args: self.toggle(str(1)),
        )
        self.toggle2 = tk.Button(
            self,
            text="Viscosity Calculator",
            font=("Garamond", 15),
            command=lambda *args: self.toggle(str(2)),
        )
        self.toggle1.grid(column=0, row=1)
        self.toggle2.grid(column=1, row=1, padx=30, pady=10)
        self.temp = bartz(self)
        self.temp.grid(column=0, row=2, columnspan=20)

    def toggle(self, var):
        if var == "1":
            self.temp.grid_remove()
            self.temp = bartz(self)
            self.temp.grid(column=0, row=2, columnspan=20)
        elif var == "2":
            self.temp.grid_remove()
            self.temp = viscosityCalculator(self)
            self.temp.grid(column=0, row=2, columnspan=20)


class bartz(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.configure(bg="#222831")

        self.parent = parent
        self.label = tk.Label(
            self,
            text="Bartz Heat Transfer Inputs",
            fg="white",
            font=("Garamond", 20),
            bg="#222831",
        )
        self.label.grid(column=0, row=0, sticky="w", pady=(10, 0))

        self.importCoord = tk.Button(
            self,
            text="Import \n Coordinates",
            fg="black",
            font=("Garamond", 20),
            command=self.UploadAction,
        )
        self.importCoord.grid(column=0, row=3, rowspan=3, sticky="w")

        self.t0 = enu(self, "Stagnation Temperature(K): ")
        self.t0.grid(column=1, row=1, sticky="w", pady=5)
        self.p0 = enu(self, "Stagnation Pressure(MPa): ")
        self.p0.grid(column=1, row=2, sticky="w")
        self.tr = enu(self, "Throat Radius(M): ")
        self.tr.grid(column=1, row=3, sticky="w", pady=5)
        self.k = enu(self, "Gamma: ")
        self.k.grid(column=1, row=4, sticky="w")
        self.t_w = enu(self, "Real Wall Temperature(K): ")
        self.t_w.grid(column=1, row=5, sticky="w", pady=5)
        self.c_p = enu(self, "Specific Heat of Exhaust: ")
        self.c_p.grid(column=1, row=6, sticky="w")
        self.recoveryFactor = enu(self, "Recovery Factor: ")
        self.recoveryFactor.grid(column=1, row=7, sticky="w", pady=5)
        self.mu_0 = enu(self, "W value: ")
        self.mu_0.grid(column=1, row=8, sticky="w")
        self.cstar = enu(self, "Characteristic Velocity(m/s): ")
        self.cstar.grid(column=1, row=9, sticky="w", pady=5)
        # self.Pr_o = (4*k.val())/((9*k.val())-5) #stagnant prental(maybe) number
        self.td = self.tr.val() * 2

    def UploadAction(self, event=None):
        filename = filedialog.askopenfilename()
        if filename[-4:] == ".csv":
            df = pd.read_csv(filename, header=None)
            df = np.array(df)
            formatdf = np.array2string(
                df, formatter={"float_kind": lambda x: "%.7f" % x}
            )
            # self.tabulatetemperature(self,df)
            height = len(df)
            self.tempRange = [0] * height
            tempStep = (4693 - 500) / height
            for i in range(1, height):
                tempRange[i] = 500 + tempStep * (i - 1)
        else:
            print("wrong file")


class viscosityCalculator(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.configure(bg="#222831")

        columnNames = [
            "Viscosity \nElement",
            "Molecular wt. \n [g/mol]",
            "Molar Fraction",
            "Boiling Point [K]",
            "Density @ boiling \n point [kg/m^3]",
            "Dipole \nMoment",
        ]
        cn = [0] * 6
        rn = [0] * 5

        flag = 0
        chemicals = [
            [0 for x in range(6)] for y in range(5)
        ]  # stores all viscosity inputs
        self.chemvar = [0] * len(chemicals)

        options = [
            "None",
            "Nitrogen (N2)",
            "Hydrogen(H2)",
            "Carbon Monoxide (CO)",
            "Carbon Dioxide (C02)",
            "Hydrochloride (HCL)",
            "Oxygen(02)",
        ]
        for i in range(0, len(chemicals)):
            self.chemvar[i] = tk.StringVar()
            self.chemvar[i].set("None")
            chemicals[i][0] = tk.OptionMenu(self, self.chemvar[i], *options)
            chemicals[i][1] = tk.Entry(
                self, width=12, font=("Franklin Gothic Medium", 11), justify="center"
            )
            chemicals[i][2] = tk.Entry(
                self, width=12, font=("Franklin Gothic Medium", 11), justify="center"
            )
            chemicals[i][3] = tk.Entry(
                self, width=12, font=("Franklin Gothic Medium", 11), justify="center"
            )
            chemicals[i][4] = tk.Entry(
                self, width=12, font=("Franklin Gothic Medium", 11), justify="center"
            )
            chemicals[i][5] = tk.Entry(
                self, width=12, font=("Franklin Gothic Medium", 11), justify="center"
            )

            chemicals[i][1].config(state="disabled")
            chemicals[i][3].config(state="disabled")
            chemicals[i][4].config(state="disabled")
            chemicals[i][5].config(state="disabled")
        for r in range(0, len(chemicals)):
            rtext = "Chem " + str(r + 1)
            rn[r] = tk.Label(
                self,
                text=rtext,
                bg=("#222831"),
                fg="white",
                font=("Franklin Gothic Medium", 12),
            )
            rn[r].grid(column=0, row=r + 2, pady=(0, 15), padx=(0, 10), sticky="nesw")
            for c in range(0, len(chemicals[r])):
                ctext = columnNames[c]
                cn[c] = tk.Label(
                    self,
                    text=ctext,
                    bg=("#222831"),
                    fg="white",
                    font=("Franklin Gothic Medium", 12),
                )
                cn[c].grid(column=c + 1, row=1)
                chemicals[r][c].grid(column=c + 1, row=r + 2, padx=15, sticky="n")

        importButton = tk.Button(
            self, text="Import Characteristics", font=("Franklin Gothic Medium", 12)
        )
        importButton.grid(column=0, row=0, pady=(25, 15), columnspan=5, sticky="w")
        self.calculateButton = tk.Button(
            self,
            text="Calcuate",
            font=("Franklin Gothic Medium", 15),
            command=lambda: self.visocistyValidation(chemicals, self.chemvar),
        )
        self.calculateButton.grid(
            column=5,
            row=10,
            pady=(25, 0),
            sticky="nesw",
            columnspan=5,
        )
        plotButton = tk.Button(
            self,
            text="Plot",
            font=("Franklin Gothic Medium", 12),
            command=lambda: self.plot(self.visc_gas_mix_a),
        )
        plotButton.grid(column=0, row=10, sticky="nesw", pady=(25, 0))
        clearButton = tk.Button(
            self,
            text="Clear",
            font=("Franklin Gothic Medium", 12),
            command=lambda: self.clear(chemicals, self.chemvar),
        )
        clearButton.grid(column=3, row=10, sticky="nesw", pady=(25, 0))
        self.validationHandling = tk.Label(
            self, text="", bg="#222831", font=("Franklin Gothic Medium", 15), fg="red"
        )
        self.validationHandling.grid(column=3, row=0, columnspan=5, pady=(25, 0))

    def visocistyValidation(self, chemicals, chemvar):
        # float checker in input columns
        chemvar = self.chemvar
        flag = False
        counter = 0
        for x in chemvar:
            if x.get() == "None":
                continue
            elif x.get() == "Hydrogen(H2)":
                self.fill_in_value(x.get(), counter, chemicals, chemvar)
            elif x.get() == "Carbon Monoxide (CO)":
                self.fill_in_value(x.get(), counter, chemicals, chemvar)
            elif x.get() == "Nitrogen (N2)":
                self.fill_in_value(x.get(), counter, chemicals, chemvar)
            elif x.get() == "Hydrochloride (HCL)":
                self.fill_in_value(x.get(), counter, chemicals, chemvar)
            elif x.get() == "Carbon Dioxide (C02)":
                self.fill_in_value(x.get(), counter, chemicals, chemvar)
            elif x.get() == "Oxygen(02)":
                self.fill_in_value(x.get(), counter, chemicals, chemvar)
            counter += 1
        self.outputlist = []
        for i in range(0, len(chemicals)):
            if chemvar[i].get() == "None":
                self.outputlist.append("None")
            elif chemvar[i].get() != "None":
                if self.rowchecker(chemicals[i]):
                    templist = []
                    for a in range(1, len(chemicals[i])):
                        templist.append(chemicals[i][a].get())
                    self.outputlist.append([chemvar[i].get()] + templist)
                elif not (self.rowchecker(chemicals[i])):
                    self.validationHandling.configure(text="Error: Invalid Input Form")
                    self.calculateButton(state="disabled")
                    return
        self.strippedOutputList = []

        for i in range(0, len(self.outputlist)):
            if self.outputlist[i] == "None":
                continue
            elif self.outputlist[i] != "None":
                self.strippedOutputList.append(self.outputlist[i])
        self.viscositycalculation(self.strippedOutputList, chemicals)

    def rowchecker(self, chemicals):
        for i in range(1, len(chemicals)):
            if self.will_it_float(chemicals[i].get()):
                continue
            elif not (self.will_it_float(chemicals[i].get())):
                return False
        return True

    def viscositycalculation(self, strippedOutputList, chemicals):

        try:
            temp = 1
            gasMixtureArray = [0] * 3500
            num = len(strippedOutputList)

            self.visc_gas_mix_a = [0] * 3500
            for aaa in range(0, 3500):
                mu_a = [0] * num
                mw_a = [0] * num
                mf_a = [0] * num
                bp_a = [0] * num
                db_a = [0] * num
                dm_a = [0] * num
                mv_a = [0] * num

                for a in range(0, num):
                    if strippedOutputList[a][0] == "Nitrogen (N2)":
                        mu_a[a] = (
                            42.606
                            + (4.75 * (10 ** -1)) * temp
                            + ((-9.88 * (10 ** -5)) * (temp ** 2))
                        ) * (10 ** -2)
                    elif strippedOutputList[a][0] == "Hydrogen(H2)":
                        mu_a[a] = (
                            27.758
                            + (2.12 * (10 ** -1)) * temp
                            + ((-3.28 * (10 ** -5)) * (temp ** 2))
                        ) * (10 ** -2)
                    elif strippedOutputList[a][0] == "Carbon Monoxide (CO)":
                        mu_a[a] = (
                            23.811
                            + (5.3944 * (10 ** -1)) * temp
                            + ((-1.5411 * (10 ** -4)) * (temp ** 2))
                        ) * (10 ** -2)
                    elif strippedOutputList[a][0] == "Carbon Dioxide (C02)":
                        mu_a[a] = (
                            11.811
                            + (4.983 * (10 ** -1)) * temp
                            + ((-1.0851 * (10 ** -4)) * (temp ** 2))
                        ) * (10 ** -2)
                    elif strippedOutputList[a][0] == "Hydrochloride (HCL)":
                        mu_a[a] = (
                            -9.118
                            + (5.55 * (10 ** -1)) * temp
                            + ((-1.11 * (10 ** -4)) * (temp ** 2))
                        ) * (10 ** -2)
                    elif strippedOutputList[a][0] == "Oxygen(02)":
                        mu_a[a] = (
                            44.224
                            + (5.6200 * (10 ** -1)) * temp
                            + ((-1.1300 * (10 ** -4)) * (temp ** 2))
                        ) * (10 ** -2)

                for a in range(0, num):
                    mw_a[a] = float(strippedOutputList[a][1])  # molecular weight array
                    mf_a[a] = float(strippedOutputList[a][2])  # molar fraction array
                    bp_a[a] = float(strippedOutputList[a][3])  # boiling point array
                    db_a[a] = float(
                        strippedOutputList[a][4]
                    )  # density at boiling point array
                    dm_a[a] = float(strippedOutputList[a][5])  # dipole moment array
                    mv_a[a] = mw_a[a] * (1 / db_a[a]) * (1 / 1000)
                num_coef = num ** 2

                m_coef = [0] * num_coef
                i = 0
                j = 0

                for a in range(0, len(m_coef)):
                    m_coef[a] = (
                        (4 * mw_a[i] * mw_a[j]) / (mw_a[i] + mw_a[j]) ** 2
                    ) ** 0.25

                    if j == num - 1:
                        j = 0
                        i = i + 1
                    else:
                        j = j + 1

                A_coef = [0] * num_coef
                num_bracket = [0] * num_coef
                denom_bracket = [0] * num_coef
                bracket = [0] * num_coef

                i = 0
                j = 0

                # A-Coefficient Logic
                for a in range(0, len(A_coef)):
                    num_bracket[a] = (mw_a[i] / mw_a[j]) - (mw_a[i] / mw_a[j]) ** 0.45
                    denom_bracket[a] = (
                        2 * (1 + (mw_a[i] / mw_a[j]))
                        + ((1 + ((mw_a[i] / mw_a[j]) ** 0.45)) / (1 + m_coef[a]))
                        * m_coef[a]
                    )
                    bracket[a] = 1 + ((num_bracket[a]) / (denom_bracket[a]))

                    A_coef[a] = m_coef[a] * ((mw_a[j] / mw_a[i]) ** 0.5) * (bracket[a])
                    if j == num - 1:
                        j = 0
                        i = i + 1
                    else:
                        j = j + 1

                # S coefficient Logic
                delta = [0] * num
                for a in range(0, len(delta)):
                    delta[a] = (2 * 10 ** 3) * (((dm_a[a]) ** 2) / (bp_a[a] * mv_a[a]))

                rduc_temp = [0] * num
                for a in range(0, len(rduc_temp)):
                    rduc_temp[a] = temp / (1.15 * bp_a[a]) * (1 + 0.85 * delta[a] ** 2)

                S_coef = [0] * num_coef
                num_scoef = [0] * num_coef
                denom_scoef = [0] * num_coef

                i = 0
                j = 0

                for a in range(0, len(S_coef)):
                    num_scoef[a] = (
                        1
                        + ((rduc_temp[i] * rduc_temp[j]) ** 0.5)
                        + ((delta[i] * delta[j]) / 4)
                    )
                    denom_scoef[a] = (
                        (1 + rduc_temp[i] + ((delta[i] ** 2) / 4)) ** 0.5
                    ) * ((1 + rduc_temp[j] + ((delta[j] ** 2) / 4)) ** 0.5)
                    S_coef[a] = (num_scoef[a]) / (denom_scoef[a])

                    if j == num - 1:
                        j = 0
                        i = i + 1
                    else:
                        j = j + 1

                i = 0
                j = 0

                if num == 2:
                    denom_sum_comp = [0] * num_coef
                    for a in range(0, len(denom_sum_comp)):
                        denom_sum_comp[a] = (S_coef[i] * A_coef[i]) * (
                            mf_a[j] / math.sqrt(mu_a[j])
                        )
                        if i == num - 1:
                            j = 0
                            i = i + 1
                        else:
                            i = i + 1
                            j = j + 1
                    denom_sum = [0] * num
                    denom_sum[0] = denom_sum_comp[1]
                    denom_sum[1] = denom_sum_comp[2]

                elif num == 3:
                    denom_sum_comp = [0] * num_coef
                    for a in range(0, len(denom_sum_comp)):
                        denom_sum_comp[a] = (S_coef[i] * A_coef[i]) * (
                            mf_a[j] / math.sqrt(mu_a[j])
                        )

                        if i == num - 1 or i == (num - 1) * 2:
                            j = 0
                            i = i + 1
                        else:
                            i = i + 1
                            j = j + 1
                    denom_sum = [0] * num
                    denom_sum[0] = denom_sum_comp[1] + denom_sum_comp[2]
                    denom_sum[1] = denom_sum_comp[3] + denom_sum_comp[5]
                    denom_sum[2] = denom_sum_comp[6] + denom_sum_comp[7]

                elif num == 4:
                    denom_sum_comp = [0] * num_coef
                    for a in range(0, len(denom_sum_comp)):
                        denom_sum_comp[a] = (S_coef[i] * A_coef[i]) * (
                            mf_a[j] / math.sqrt(mu_a[j])
                        )

                        if i == (num - 1) or i == (num - 1) * 2 or i == (num - 1) * 3:
                            j = 0
                            i = i + 1
                        else:
                            i = i + 1
                            j = j + 1
                    denom_sum = [0] * num
                    denom_sum[0] = (
                        denom_sum_comp[1] + denom_sum_comp[2] + denom_sum_comp[3]
                    )
                    denom_sum[1] = (
                        denom_sum_comp[4] + denom_sum_comp[6] + denom_sum_comp[7]
                    )
                    denom_sum[2] = (
                        denom_sum_comp[8] + denom_sum_comp[9] + denom_sum_comp[11]
                    )
                    denom_sum[3] = (
                        denom_sum_comp[12] + denom_sum_comp[13] + denom_sum_comp[14]
                    )
                elif num == 5:
                    denom_sum_comp = [0] * num_coef
                    for a in range(0, len(denom_sum_comp)):
                        denom_sum_comp[a] = (S_coef[i] * A_coef[i]) * (
                            mf_a[j] / math.sqrt(mu_a[j])
                        )

                        if (
                            i == (num - 1)
                            or i == (num - 1) * 2
                            or i == (num - 1) * 3
                            or i == (num - 1) * 4
                        ):
                            j = 0
                            i = i + 1
                        else:
                            i = i + 1
                            j = j + 1
                    denom_sum = [0] * num
                    denom_sum[0] = (
                        denom_sum_comp[1]
                        + denom_sum_comp[2]
                        + denom_sum_comp[3]
                        + denom_sum_comp[4]
                    )
                    denom_sum[1] = (
                        denom_sum_comp[5]
                        + denom_sum_comp[7]
                        + denom_sum_comp[8]
                        + denom_sum_comp[9]
                    )
                    denom_sum[2] = (
                        denom_sum_comp[10]
                        + denom_sum_comp[11]
                        + denom_sum_comp[13]
                        + denom_sum_comp[14]
                    )
                    denom_sum[3] = (
                        denom_sum_comp[15]
                        + denom_sum_comp[16]
                        + denom_sum_comp[17]
                        + denom_sum_comp[19]
                    )
                    denom_sum[4] = (
                        denom_sum_comp[20]
                        + denom_sum_comp[21]
                        + denom_sum_comp[22]
                        + denom_sum_comp[23]
                    )
                else:
                    print("error")
                    break
                visc_mix = [0] * num
                for a in range(0, len(visc_mix)):
                    visc_mix[a] = (mf_a[a] * math.sqrt(mu_a[a])) / (
                        (mf_a[a] / math.sqrt(mu_a[a])) + denom_sum[a]
                    )

                visc_mix_gas = sum(visc_mix)
                self.visc_gas_mix_a[aaa] = visc_mix_gas
                temp = temp + 1
            with open("viscosity_results.csv", "w", newline="") as incsv:
                wr = csv.writer(incsv)
                for i in range(0, 3500):
                    wr.writerow([i + 1] + [self.visc_gas_mix_a[i]])
            self.validationHandling.configure(text="Success", fg="green")
            self.pltFlag = True
            self.calculateButton.config(state="disabled")
        except:
            self.validationHandling.configure(text="Error", fg="red")

    def plot(self, visc_gas_mix_a):
        matplotlib.use("TkAgg")

        top = tk.Toplevel()
        figure = Figure(figsize=(5, 4), dpi=100)
        plot = figure.add_subplot(1, 1, 1)
        # plot.plot(self.visc_gas_mix_a[-1], 3500, color="blue", marker="o", linestyle="")
        x = [*range(1, 3501, 1)]
        y = self.visc_gas_mix_a
        plot.plot(x, y, color="red", linestyle=":")

        canvas = FigureCanvasTkAgg(figure, top)
        canvas.get_tk_widget().grid(row=0, column=0)

        label = tk.Label(
            top,
            text="X Axis: Temperature (Kelvin)  \n Y Axis: Viscosity (Kg/m*s * 10^-5)",
            anchor="e",
        )
        label.grid(row=1, column=0)

        figure = Figure(figsize=(5, 4), dpi=100)

    def importCharacteristics(self):
        from pages.propellant import outsidep

        k = outsidep.composition.items()
        flag = False
        for i in k:
            x = i[1][0:5]
            flag = True
            if flag:
                break
        constituents = x

    def fill_in_value(self, var, index, chemicals, chemvar):
        from data.viscosity_data import viscdict

        chemicals[index][1].config(state="normal")
        chemicals[index][3].config(state="normal")
        chemicals[index][4].config(state="normal")
        chemicals[index][5].config(state="normal")

        chemicals[index][1].insert(0, viscdict[var][0])
        chemicals[index][3].insert(0, viscdict[var][1])
        chemicals[index][4].insert(0, viscdict[var][2])
        chemicals[index][5].insert(0, viscdict[var][3])

    def clear(self, chemicals, chemvar):
        for i in range(0, len(chemicals)):
            chemvar[i].set("None")
            chemicals[i][1].delete(0, "end")
            chemicals[i][2].delete(0, "end")
            chemicals[i][3].delete(0, "end")
            chemicals[i][4].delete(0, "end")
            chemicals[i][5].delete(0, "end")

            chemicals[i][1].config(state="disabled")
            chemicals[i][3].config(state="disabled")
            chemicals[i][4].config(state="disabled")
            chemicals[i][5].config(state="disabled")
        self.calculateButton.config(state="normal")
        self.validationHandling.configure(text="")

    def will_it_float(self, val):
        try:
            float(val)
            return float(val) >= 0
        except ValueError:
            return False
