import tkinter as tk
from tkinter import filedialog
from widgets.entry_nounit import entry_nounit as enu
from widgets.transpose import transpose
import math as m, csv
import pandas as pd
import numpy as np
import matplotlib
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


"""cm = (k - 1) / 2
cp = (k + 1) / 2
cpm = (k + 1) / (2 * (k - 1))"""


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
        self.importFile = ""
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
            text="Import Coordinates",
            fg="black",
            font=("Garamond", 15),
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
        self.importStatus = tk.Label(self, text="", fg="white", font=("Garamond", 15))
        self.importStatus.grid(column=1, row=5)
        self.calculate_button = tk.Button(
            self, text="Calculate", fg="black", font=("Garamond", 20), width=15
        )
        self.calculate_button.config(state="disabled")
        self.calculate_button.grid(column=2, row=10, pady=15)
        # self.Pr_o = (4*k.val())/((9*k.val())-5) #stagnant prental(maybe) number
        self.td = self.tr.val() * 2

    def UploadAction(self, event=None):
        filename = filedialog.askopenfilename()
        if filename[-4:] == ".csv":
            df = pd.read_csv(filename, header=None)
            df = np.array(df)
            print(len(df[0]))
            if (
                len(df[0]) == 3 and len(df) > 30
            ):  # need a more concrete parameter for validation
                self.importStatus.configure(text="Import Successful")
                self.importFile = filename
                self.calculate_button.config(state="normal")
            else:
                self.importStatus.configure(text="Incorrect File Format")
                self.calculate_button.config(state="disabled")
        else:
            pass

    def calculate(self, filename):
        df = pd.read_csv(filename, header=None)
        df = np.arrray(df)
        formatdf = np.array2string(df, formatter={"float_kind": lambda x: "%.7f" % x})
        height = len(df)
        self.varMatrix = [0] * 11
        A_t = math.pi * (tr ** 2)
        # h_g_const = (.026/(dStar^.2))*(((mu_o^.2)*c_p)/(Pr_o^.6))*(((p_o*g)/cStar)^.8)

    def machIter(self, data, height):
        stepSize = 0.00005
        maxIteration = 20000
        convCond = 0.0005
        lastMach = 1
        self.machArray = []
        for i in range(0, height):

            converged = False
            r = round(df[i][1], 7)
            firstR = round(df[0][1], 7)
            rRatioTarget = (r / rStar) ** 2
            currentIteration = 1
            low = 1
            high = exitMach + 0.5
            counter = 0
            while converged == False and low <= high:
                mid = (low + high) / 2
                M = mid
                testCase = (1 / M) * ((1 + cm * (M ** 2) / cp) ** cpm)
                if round(df[i][1], 7) == firstR:
                    converged = True
                    M = 1.0
                elif abs(testCase - rRatioTarget) <= convCond:
                    converged = True
                else:

                    if testCase < rRatioTarget:
                        low = mid + stepSize
                    elif testCase > rRatioTarget:
                        high = mid - stepSize

            self.machArray.append(M)
        return self.machArray

    def tabulateTemperature(self, data, height):
        temp = []
        for i in range(0, height):
            M = self.machArray[i]
            T = 2 * T_o / (2 + (k * (M ** 2)) - M ** 2)
            temp.append(T)
        return temp

    def tabulateFlowDensity(self, data, height):
        pU_numerator_const = ((32.174 / 778.2) ** (1 / 2)) * k * p_o
        pU_denominator_const = (c_p * T_o * (k - 1)) ** (1 / 2)
        temp = []
        for i in range(0, height):
            M = self.machArray[i]
            temp.append(
                (pU_numerator_const * M)
                / (pU_denominator_const * (1 + cm * (M ** 2)) ** cpm)
            )
        return temp

    def tabulateAdiabaticWallTemperature(self, data, height):
        temp = []
        for i in range(0, height):
            M = self.machArray[i]
            T_aw = ((1 + recoveryFactor * cm * (M ** 2)) / (1 + cm * (M ** 2))) * T_o
            temp.append(T_aw)
        return temp

    def tabulateIntegralConstants(self, data, height):
        aMatrix = []
        bMatrix = []
        cMatrix = []
        for i in range(0, height):
            M = self.machArray[i]
            aMatrix.append(T_w / self.varMatrix[4][i])
            bMatrix.append((T_o / T_w) - 1)
            cMatrix.append((cm * (M ** 2)) * (self.varMatrix[4][i] / T_w))

        return aMatrix, bMatrix, cMatrix

    def tabulatePressureAlongNozzle(self, data, height):
        temp = []
        for i in range(0, height):
            M = self.machArray[i]
            temp.append(p_o / ((1 + (0.5 * (k - 1) * M ^ 2)) ** (k / (k - 1))))
        return temp


"""
zStation_matrix = 1;        %x is defined as zStation as that is the format that the bartz paper takes
r_matrix = 2;               %radius
p_matrix = 3;               %pressure
M_matrix = 4;               %mach number
T_matrix = 5;               %temperature matrix
pU_matrix = 6;              %flow density
T_aw_matrix = 7;            %adiabatic wall temperature
a_matrix = 8;               %integral constant              
b_matrix = 9;               %integral constant    
c_matrix = 10;              %integral constant    
h_g_matrix = 11;            %closed form bartz heat transfer coeff
"""


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
            command=lambda: self.plot(self.visc_gas_mix_a, self.gas_therm_a),
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

        temp = 50
        gasMixtureArray = [0] * 3400
        num = len(strippedOutputList)

        self.visc_gas_mix_a = [0] * 3400
        self.gas_therm_a = [0] * 3400

        for aaa in range(0, 3400):
            mu_a = [0] * num
            mw_a = [0] * num
            mf_a = [0] * num
            bp_a = [0] * num
            db_a = [0] * num
            dm_a = [0] * num
            mv_a = [0] * num
            therm_a = [0] * num
            sigma_a = [0] * num
            ek_a = [0] * num

            for a in range(0, num):
                if strippedOutputList[a][0] == "Nitrogen (N2)":
                    mu_a[a] = (
                        42.606
                        + (4.75 * 10 ** -1) * temp
                        + ((-9.88 * 10 ** -5) * temp ** 2)
                    ) * (10 ** -2)
                    therm_a[a] = (
                        0.00309
                        + (7.5930 * (10 ** -5)) * temp
                        + ((-1.1014 * (10 ** -8)) * temp ** 2)
                    )
                    sigma_a[a] = 3.798
                    ek_a[a] = 71.4

                elif strippedOutputList[a][0] == "Hydrogen(H2)":
                    mu_a[a] = (
                        27.758
                        + (2.12 * 10 ** -1) * temp
                        + ((-3.28 * 10 ** -5) * temp ** 2)
                    ) * (10 ** -2)
                    therm_a[a] = (
                        0.03951
                        + (4.5918 * 10 ** -4) * temp
                        + ((-6.4933 * 10 ** -8) * temp ** 2)
                    )
                    sigma_a[a] = 2.827
                    ek_a[a] = 59.7

                elif strippedOutputList[a][0] == "Carbon Monoxide (CO)":
                    mu_a[a] = (
                        23.811
                        + (5.3944 * (10 ** -1)) * temp
                        + ((-1.5411 * (10 ** -4)) * (temp ** 2))
                    ) * (10 ** -2)
                    therm_a[a] = (
                        0.00158
                        + (8.2511 * 10 ** -5) * temp
                        + ((-1.9081 * (10 ** -8)) * temp ** 2)
                    )
                    sigma_a[a] = 3.690
                    ek_a[a] = 91.7

                elif strippedOutputList[a][0] == "Carbon Dioxide (C02)":
                    mu_a[a] = (
                        11.811
                        + (4.983 * (10 ** -1)) * temp
                        + ((-1.0851 * (10 ** -4)) * (temp ** 2))
                    ) * (10 ** -2)
                    therm_a[a] = (
                        -0.01200
                        + (1.0208 * 10 ** -4) * temp
                        + ((-2.2403 * 10 ** -8) * temp ** 2)
                    )
                    sigma_a[a] = 3.941
                    ek_a[a] = 195.2

                elif strippedOutputList[a][0] == "Hydrochloride (HCL)":
                    mu_a[a] = (
                        -9.118
                        + (5.55 * (10 ** -1)) * temp
                        + ((-1.11 * (10 ** -4)) * (temp ** 2))
                    ) * (10 ** -2)
                    therm_a[a] = (
                        0.00119
                        + (4.4775 * 10 ** -5) * temp
                        + ((2.0997 * 10 ** -10) * temp ** 2)
                    )
                    sigma_a[a] = 3.39
                    ek_a[a] = 344.7

                elif strippedOutputList[a][0] == "Oxygen(02)":
                    mu_a[a] = (
                        44.224
                        + (5.6200 * (10 ** -1)) * temp
                        + ((-1.1300 * (10 ** -4)) * (temp ** 2))
                    ) * (10 ** -2)
                elif strippedOutputList[a][0] == "Helium (He)":
                    mu_a[w] = (
                        7.29 + (0.03884) * temp + ((-1.937 * 10 ** -6) * temp ** 2)
                    ) * (10 ** -2)
                    therm_a[a] = (
                        47.25 + (0.3127) * temp + ((-1.688 * 10 ** -5) * temp ** 2)
                    ) * (10 ** -3)
                    sigma_a[a] = 3.608
                    ek_a[a] = 10.22

                elif strippedOutputList[a][0] == "Neon (Ne)":
                    mu_a[a] = (
                        10.22 + (0.06096) * temp + ((-4.265 * 10 ** -6) * temp ** 2)
                    ) * (10 ** -2)
                    therm_a[a] = (
                        15.98 + (0.09441) * temp + ((-6.604 * 10 ** -6) * temp ** 2)
                    ) * (10 ** -3)
                    sigma_a[a] = 2.820
                    ek_a[a] = 32.8

                elif strippedOutputList[a][0] == "Xenon (Xe)":
                    mu_a[a] = (
                        7.755 + (0.05746) * temp + ((-4.062 * 10 ** -6) * temp ** 2)
                    ) * (10 ** -2)
                    therm_a[a] = (
                        1.887 + (0.01366) * temp + ((-9.619 * 10 ** -7) * temp ** 2)
                    ) * (10 ** -3)
                    sigma_a[a] = 4.082
                    ek_a[a] = 206.9

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
                m_coef[a] = ((4 * mw_a[i] * mw_a[j]) / (mw_a[i] + mw_a[j]) ** 2) ** 0.25

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
                denom_scoef[a] = ((1 + rduc_temp[i] + ((delta[i] ** 2) / 4)) ** 0.5) * (
                    (1 + rduc_temp[j] + ((delta[j] ** 2) / 4)) ** 0.5
                )
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
                        mf_a[j] / m.sqrt(mu_a[j])
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
                        mf_a[j] / m.sqrt(mu_a[j])
                    )

                    if i == num - 1 or i == (num * 2) - 1:
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
                        mf_a[j] / m.sqrt(mu_a[j])
                    )

                    if i == (num - 1) or i == (num * 2) - 1 or i == (num * 3) - 1:
                        j = 0
                        i = i + 1
                    else:
                        i = i + 1
                        j = j + 1
                denom_sum = [0] * num
                denom_sum[0] = denom_sum_comp[1] + denom_sum_comp[2] + denom_sum_comp[3]
                denom_sum[1] = denom_sum_comp[4] + denom_sum_comp[6] + denom_sum_comp[7]
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
                        mf_a[j] / m.sqrt(mu_a[j])
                    )

                    if (
                        i == (num - 1)
                        or i == (num * 2) - 1
                        or i == (num * 3) - 1
                        or i == (num * 4) - 1
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
                self.validationHandling.configure(text="Error", fg="red")
                self.calculateButton.config(state="disabled")
                raise ValueError("Error")
            visc_mix = [0] * num
            for a in range(0, len(visc_mix)):
                visc_mix[a] = (mf_a[a] * m.sqrt(mu_a[a])) / (
                    (mf_a[a] / m.sqrt(mu_a[a])) + denom_sum[a]
                )

            visc_mix_gas = sum(visc_mix)
            self.visc_gas_mix_a[aaa] = visc_mix_gas
            sigma_aa = [[0 for x in range(num)] for y in range(num)]
            ek_aa = [[0 for x in range(num)] for y in range(num)]
            t_star = [[0 for x in range(num)] for y in range(num)]
            omega_22 = [[0 for x in range(num)] for y in range(num)]
            omega_12 = [[0 for x in range(num)] for y in range(num)]
            omega_13 = [[0 for x in range(num)] for y in range(num)]
            omega_11 = [[0 for x in range(num)] for y in range(num)]
            a_parameter = [[0 for x in range(num)] for y in range(num)]
            b_parameter = [[0 for x in range(num)] for y in range(num)]
            visc_ij = [[0 for x in range(num)] for y in range(num)]
            therm_ij = [[0 for x in range(num)] for y in range(num)]
            num_therm = [[0 for x in range(num)] for y in range(num)]

            from widgets.check_negative import check_negative

            for i in range(0, num):
                for j in range(0, num):
                    sigma_aa[i][j] = 0.5 * (sigma_a[i] + sigma_a[j])
            # print("sigma_aa: " + str(check_negative(sigma_aa)))

            for i in range(0, num):
                for j in range(0, num):
                    ek_aa[i][j] = m.sqrt(ek_a[i] * ek_a[j])
            # print("ek_aa: " + str(check_negative(ek_aa)))
            print(temp)
            for ek in ek_aa:
                print(ek)

            for i in range(0, num):
                for j in range(0, num):
                    if ek_aa[i][j] == 0:
                        continue
                    t_star[i][j] = (1 / ek_aa[i][j]) * temp

            # print("t_star: " + str(check_negative(t_star)))
            print(t_star)

            for w in range(0, num):
                for z in range(0, num):
                    x = t_star[z][w]
                    omega_22[z][w] = (
                        (1.586)
                        + (-0.7882) * m.log(x)
                        + (0.2938) * m.log(x) ** 2
                        + (0.008756) * m.log(x) ** 3
                        + (-0.05198) * m.log(x) ** 4
                        + (0.01936) * m.log(x) ** 5
                        + (-0.003264) * m.log(x) ** 6
                        + (0.0002639) * m.log(x) ** 7
                        + (-8.135 * (10 ** -6)) * m.log(x) ** 8
                    )
            print("omega_22: " + str(check_negative(omega_22)))

            for w in range(0, num):
                for z in range(0, num):
                    x = t_star[z][w]
                    omega_12[z][w] = (
                        1.204
                        + (-0.5152) * m.log(x)
                        + (0.2609) * m.log(x) ** 2
                        + (-0.06649) * m.log(x) ** 3
                        + (-0.01035) * m.log(x) ** 4
                        + (0.01155) * m.log(x) ** 5
                        + (-0.003077) * m.log(x) ** 6
                        + (0.000366) * m.log(x) ** 7
                        + (-1.671 * (10 ** -5)) * m.log(x) ** 8
                    )
            print("omega_12: " + str(check_negative(omega_12)))

            for w in range(0, num):
                for z in range(0, num):
                    x = t_star[z][w]
                    omega_13[z][w] = (
                        1.076
                        + (-0.3846) * m.log(x)
                        + (0.2081) * m.log(x) ** 2
                        + (-0.0752) * m.log(x) ** 3
                        + (0.005667) * m.log(x) ** 4
                        + (0.005235) * m.log(x) ** 5
                        + (-0.001856) * m.log(x) ** 6
                        + (0.0002466) * m.log(x) ** 7
                        + (-1.199 * (10 ** -5)) * m.log(x) ** 8
                    )
            print("omega_13: " + str(check_negative(omega_13)))

            for w in range(0, num):
                for z in range(0, num):
                    x = t_star[z][w]
                    omega_11[z][w] = (
                        1.44
                        + (-0.7037) * m.log(x)
                        + (0.286) * m.log(x) ** 2
                        + (-0.03118) * m.log(x) ** 3
                        + (-0.02613) * m.log(x) ** 4
                        + (0.0127) * m.log(x) ** 5
                        + (-0.002519) * m.log(x) ** 6
                        + (0.0002424) * m.log(x) ** 7
                        + (-9.291 * (10 ** -6)) * m.log(x) ** 8
                    )
            print("omega_11: " + str(check_negative(omega_11)))

            for i in range(0, num):
                for j in range(0, num):
                    a_parameter[i][j] = omega_22[i][j] / omega_11[i][j]
            print("a_parameter: " + str(check_negative(a_parameter)))

            for i in range(0, num):
                for j in range(0, num):
                    b_parameter[i][j] = (5 * omega_12[i][j] - 4 * omega_13[i][j]) / (
                        omega_11[i][j]
                    )
            print("b_parameter: " + str(check_negative(b_parameter)))

            for i in range(0, num):
                for j in range(0, num):
                    visc_ij[i][j] = 266.93 * (
                        m.sqrt((2 * mw_a[i] * mw_a[j] * temp) / (mw_a[i] + mw_a[j]))
                        / ((sigma_aa[i][j]) ** 2 * omega_22[i][j])
                    )
                    visc_ij[i][j] = visc_ij[i][j] * 10 ** (-7) * 0.1
            print("visc_ij: " + str(check_negative(visc_ij)))

            for i in range(0, num):
                for j in range(0, num):
                    num_therm[i][j] = m.sqrt(
                        (temp * (mw_a[i] + mw_a[j])) / (w * mw_a[i] * mw_a[j])
                    )
                    therm_ij[i][j] = 1989.1 * (
                        (num_therm[i][j]) / ((sigma_aa[i][j]) ** w * omega_22[i][j])
                    )
                    therm_ij[i][j] = therm_ij[i][j] * (10 ** -7) * 418.4

            sub_phi_ij_coef = [[0 for x in range(num)] for y in range(num)]

            for i in range(0, len(mu_a)):
                mu_a[i] = mu_a[i] * (10 ** -4)

            for i in range(0, num):
                for j in range(0, num):
                    sub_phi_ij_coef[i][j] = ((mu_a[i]) / visc_ij[i][j]) * (
                        (2 * mw_a[j]) / (mw_a[i] + mw_a[j])
                    )

            sub_phi_ji_coef = transpose(sub_phi_ij_coef)

            test = [[0 for x in range(num)] for y in range(num)]

            """for i in range(0, num):
                for j in range(0, num):
                    if sub_phi_ij_coef[i][j] == 0 or sub_phi_ji_coef[i][j] == 0:
                        continue
                    test[i][j] = (
                        m.sqrt(sub_phi_ij_coef[i][j]) + m.sqrt(sub_phi_ji_coef[i][j])
                    ) * (1 + m.sqrt(sub_phi_ij_coef[i][j] * sub_phi_ji_coef[i][j])) ** (
                        -1
                    )"""

            phi_coef = [[0 for x in range(num)] for y in range(num)]
            num_phi = [[0 for x in range(num)] for y in range(num)]
            denom_phi = [[0 for x in range(num)] for y in range(num)]
            f_coef_ij = [[0 for x in range(num)] for y in range(num)]
            bracket_ij = [[0 for x in range(num)] for y in range(num)]

            for i in range(0, num):
                for j in range(0, num):
                    num_phi[i][j] = mw_a[i] * m.sqrt(sub_phi_ij_coef[i][j]) - mw_a[
                        j
                    ] * m.sqrt(sub_phi_ji_coef[i][j])
                    denom_phi[i][j] = 2 * (mw_a[i] + mw_a[j]) + mw_a[j] * m.sqrt(
                        sub_phi_ji_coef[i][j]
                    )
                    phi_coef[i][j] = sub_phi_ij_coef[i][j] + (
                        num_phi[i][j] / denom_phi[i][j]
                    ) * m.sqrt(sub_phi_ij_coef[i][j])

            for i in range(0, num):
                for j in range(0, num):
                    bracket_ij[i][j] = ((15 / (4 * a_parameter[i][j])) - 1) * (
                        mw_a[i] - mw_a[j]
                    ) + (
                        ((3 * b_parameter[i][j]) / (2 * a_parameter[i][j]))
                        + (5 / (8 * a_parameter[i][j]))
                    ) * mw_a[
                        j
                    ]
                    f_coef_ij[i][j] = 1 + (
                        (mw_a[i] - mw_a[j]) / (mw_a[i] + mw_a[j]) ** 2
                    ) * (bracket_ij[i][j])

            f_coef_ji = transpose(f_coef_ij)

            sub_psi_coef_ij = [[0 for x in range(num)] for y in range(num)]

            for i in range(0, num):
                for j in range(0, num):
                    sub_psi_coef_ij[i][j] = sub_phi_ij_coef[i][j] * f_coef_ij[i][j]

            sub_psi_coef_ji = transpose(sub_psi_coef_ij)

            test2 = [[0 for x in range(num)] for y in range(num)]
            for i in range(0, num):
                for j in range(0, num):
                    test2[i][j] = (
                        m.sqrt(sub_psi_coef_ij[i][j]) + m.sqrt(sub_psi_coef_ji[i][j])
                    ) * (1 + m.sqrt(sub_psi_coef_ij[i][j] * sub_psi_coef_ji[i][j])) ** (
                        -1
                    )

            psi_coef = [[0 for x in range(num)] for y in range(num)]
            num_psi = [[0 for x in range(num)] for y in range(num)]
            denom_psi = [[0 for x in range(num)] for y in range(num)]

            for i in range(0, num):
                for j in range(0, num):
                    num_psi[i][j] = (
                        m.sqrt(sub_psi_coef_ij[i][j]) / f_coef_ij[i][j]
                    ) - (m.sqrt(sub_psi_coef_ji[i][j]) / f_coef_ji[i][j])
                    denom_psi[i][j] = (
                        ((mw_a[i] + mw_a[j]) ** 2) / (2.6 * mw_a[i] * mw_a[j])
                    ) + (m.sqrt(sub_psi_coef_ji[i][j] / f_coef_ji[i][j]))
                    psi_coef[i][j] = sub_psi_coef_ij[i][j] + (
                        num_psi[i][j] / denom_psi[i][j]
                    ) * m.sqrt(sub_psi_coef_ij[i][j])

            denom_sum_comp = [[0 for x in range(num)] for y in range(num)]

            for i in range(0, num):
                for j in range(0, num):
                    if j == i:
                        denom_sum_comp[i][j] = 0
                    else:
                        denom_sum_comp[i][j] = psi_coef[i][j] * mf_a[j]

            # denom_sum = sum(transpose(denom_sum_comp))
            denom_sum_comp_transpose = transpose(denom_sum_comp)
            denom_sum = [0] * num
            for i in range(0, num):
                for j in range(0, num):
                    denom_sum[i] += denom_sum_comp_transpose[j][i]

            therm_mix = [0] * num
            for w in range(0, len(therm_mix)):
                therm_mix[w] = (mf_a[w] * therm_a[w]) / (mf_a[w] + denom_sum[w])

            gas_therm = sum(therm_mix)

            polar_gas_logic = 0
            dm_logic = []
            for i in dm_a:
                dm_logic.append(i / (3.335640 * (10 ** -30)))
            # dm_logic = (dm_a) / (3.335640 * 10 ** -30)

            for w in range(0, num):
                if dm_logic[w] > 0.1:
                    polar_gas_logic = polar_gas_logic + 1
                elif dm_logic[w] <= 0.1:
                    polar_gas_logic = polar_gas_logic

            if polar_gas_logic != 0:
                self.gas_therm_a[aaa] = gas_therm * 10
            elif polar_gas_logic == 0:
                self.gas_therm_a[aaa] = gas_therm

            temp = temp + 1

        with open("viscosity_results.csv", "w", newline="") as incsv:
            wr = csv.writer(incsv)
            for i in range(0, 3400):
                wr.writerow([i + 1] + [self.visc_gas_mix_a[i]])

        with open("conductivity_results.csv", "w", newline="") as incsv:
            wr = csv.writer(incsv)
            for i in range(0, 3400):
                wr.writerow([i + 1] + [self.gas_therm_a[i]])

        self.validationHandling.configure(text="Success", fg="green")
        self.pltFlag = True
        self.calculateButton.config(state="disabled")

    def plot(self, visc_gas_mix_a, gas_therm_a):
        from widgets.plot import plot_frame

        plot_frame(
            "Viscosity Results",
            6,
            3400,
            3400,
            visc_gas_mix_a,
            "X Axis: Temperature (Kelvin)  \n Y Axis: Viscosity (Kg/m*s * 10^-5)",
        )
        plot_frame(
            "Thermal Conductivity Results",
            6,
            3400,
            3400,
            gas_therm_a,
            "X Axis: Temperature (Kelvin)  \n Y Axis: Thermal Conductivity (Kg/m*s * 10^-5)",
        )

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
