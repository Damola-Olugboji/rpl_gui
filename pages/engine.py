import tkinter as tk
from widgets.entry_unit import entry_with_unit as ewu
from widgets.checkbox import checkbox as chk
from calculations.tree_results import tree
import math, csv


class engine_calculations(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.frame = tk.Frame(self)
        self.frame.grid(column=0, row=0, sticky="nesw")
        self.parent = parent
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # add padding every 2nd row
        self.p1 = ewu(self, "Chamber Pressure: ", ["PSI"])
        self.p1.grid(column=0, row=1, pady=10, sticky="w")
        self.t1 = ewu(self, "Chamber Temperature: ", ["K", "R", "C", "F"])
        self.t1.grid(column=0, row=2, sticky="w")
        self.pe = ewu(self, "Ambient Pressure: ", ["PSI"])
        self.pe.grid(column=0, row=3, pady=10, sticky="w")
        self.F = ewu(self, "Thrust Desired: ", ["N"])
        self.F.grid(column=0, row=4, sticky="w")
        self.k = ewu(self, "Gamma: ", [""])
        self.k.grid(column=0, row=5, padx=0, pady=10, sticky="w")
        self.configure(bg="#222831")
        self.var = 0
        self.var = tk.IntVar()
        self.cp = tk.Checkbutton(
            self,
            onvalue=1,
            offvalue=0,
            variable=self.var,
            text="Optional",
            fg="#1EA51D",
            bg="#222831",
            command=self.hide,
            font=("Franklin Gothic Demi", 15),
            activebackground="#222831",
            cursor="hand2",
            activeforeground="#1EA51D",
        )
        self.cp.grid(column=0, row=6, pady=(20, 0), sticky="w")
        self.i_t = ewu(self, "Desired Total Impulse: ", ["N-s"])
        self.g1var = tk.IntVar()
        self.graph1 = tk.Checkbutton(
            self,
            text="Display Altitude/Thrust graph",
            fg="#1EA51D",
            bg="#222831",
            offvalue=0,
            onvalue=1,
            font=("Franklin Gothic Medium", 12),
            variable=self.g1var,
            activebackground="#222831",
            activeforeground="#1EA51D",
            cursor="hand2",
        )
        self.g2var = tk.IntVar()
        self.graph2 = tk.Checkbutton(
            self,
            text="Display Specific Impulse Over Time graph",
            fg="#1EA51D",
            bg="#222831",
            offvalue=0,
            onvalue=1,
            cursor="hand2",
            font=("Franklin Gothic Medium", 12),
            variable=self.g2var,
            activebackground="#222831",
            highlightcolor="white",
            activeforeground="#1EA51D",
        )
        self.g3var = tk.IntVar()
        self.graph3 = tk.Checkbutton(
            self,
            text="Display Thrust Coefficient / Altitude Graph",
            fg="#1EA51D",
            bg="#222831",
            offvalue=0,
            onvalue=1,
            cursor="hand2",
            font=("Franklin Gothic Medium", 12),
            variable=self.g3var,
            activebackground="#222831",
            highlightcolor="white",
            activeforeground="#1EA51D",
        )
        self.display_results = tk.Button(
            self,
            text="Display Results",
            bg="#1EA51D",
            fg="white",
            width=20,
            font=("Garamond", 18),
            command=lambda: self.calculate(
                self.p1, self.t1, self.pe, self.F, self.k, self.i_t
            )
            # add parameters
        )
        self.display_results.grid(column=1, row=0, padx=(100, 0), rowspan=2)
        self.status = tk.Label(
            self,
            text="OUTPUTS NOT UPDATED",
            font=("Garamond", 15),
            fg="white",
            bg="#222831",
        )
        self.status.grid(column=1, row=2, padx=(100, 0))

    def hide(self):
        if self.var.get() == 0:
            self.i_t.grid_remove()
            self.graph1.grid_remove()
            self.graph2.grid_remove()
            self.graph3.grid_remove()
        else:
            self.graph1.grid(column=0, row=8, padx=0, sticky="w")
            self.graph2.grid(column=0, row=9, padx=0, sticky="w")
            self.graph3.grid(column=0, row=10, padx=0, sticky="w")
            self.i_t.grid(column=0, row=7, sticky="w", padx=(0, 0), pady=5)

    def calculate(self, p_1, t_1, p_3, F, k, i_t):
        try:
            p1 = p_1.val()  # convert all MPa
            t1 = t_1.val()
            p3 = p_3.val()
            it = i_t.val()

            F = F.val()  # don't need units, use N
            k = k.val()  # don't need units
            R = 8.3145 / 0.022745  # need molecular weight input for R value
            t2 = t1 * ((p3 / p1) ** ((k - 1) / k))

            # chamber temperature: convert all to kelvin
            if t_1.unit == "K":
                t1 = t1
            elif t_1.unit() == "R":
                t1 = t1
            elif t_1.unit() == "F":
                t1 = (t1 - 32) * (5 / 9) + 273.15
            elif t_1.unit() == "C":
                t1 = t1 + 273.15

            vt = math.sqrt(((2 * k) / (k + 1)) * (R * t1))
            V1 = (R * t1) / (p1 * 6894.75729)
            V2 = V1 * ((p1 / p3) ** (1 / k))
            Vt = V1 * (((k + 1) / 2) ** (1 / (k - 1)))
            v2 = math.sqrt(
                (((2 * k) / (k - 1)) * (t1 * R))
                * (1 - (((p3 / 145) / (p1 / 145)) ** ((k - 1) / k)))
            )
            mass_flow = F / v2
            A2 = (((mass_flow * V2) / v2) * 10 ** 4) / 6.452
            M = v2 / math.sqrt(k * R * t2)
            At = (((mass_flow * Vt) / vt) * 10 ** 4) / 6.452
            ex = A2 / At
            r = math.sqrt((At) / math.pi)
            p_t = p1 * (2 / (k + 1)) ** (k / (k - 1))
            T_t = (2 * t1) / (k + 1)  # throat static temperature 3-22

            rho_0 = (p1) / (
                R * t1
            )  # Gaseous Reactant Chamber Density (Calculated; Theoretical)

            vol_spec_0 = 1 / rho_0
            pr = p3 / p1
            cf = math.sqrt(
                ((2 * (k ** 2)) / (k - 1))
                * ((2 / (k + 1)) ** ((k + 1) / (k - 1)))
                * (1 - (pr) ** ((k - 1) / k))
            )

            vol_spec_t = (vol_spec_0) * ((k + 1) / 2) ** (
                1 / (k - 1)
            )  # static throat specific volume theoreical
            if it == "nan":
                t_b = "nan"
            else:
                # burn time - multiplied by 1.05 to account for slivers in propellant
                t_b = (it / F) * 1.05

            output = [
                ["Chamber Pressure", round(p1 / 145, 5), "MPa"],
                ["Chamber Temperature", round(t1, 5), "K"],
                ["Throat Velocity", round(vt, 5), "m/s"],
                ["Throat Pressure", round(p_t / 145, 5), "MPa"],
                ["Throat Temperature", round(T_t, 5), "K"],
                ["Throat Area", round(At, 5), "In^2"],
                ["Throat Radius", round(r, 5), "IN"],
                ["Nozzle Exit Velocity", round(v2, 5), "m/s"],
                ["Nozzle Exit Area", round(A2, 5), "IN^2"],
                ["Exit Mach Number", round(M, 5), "M"],
                ["Average Thrust", round(F, 5), "N"],
                ["Gamma", k, ""],
                ["Expansion Ratio A2/At", round(ex, 5), ""],
                ["Burn Time", t_b, "s"],
                ["Static Throat Specific Volume", round(vol_spec_t, 5), "m^3/kg"],
                ["Gaseous Product Chamber Density", round(rho_0, 5), "Kg/m^3"],
                ["Thrust Coefficient", round(cf, 5), ""],
            ]

            with open("calculations/results.csv", "w", newline="") as incsv:
                wr = csv.writer(incsv)
                for i in range(0, len(output)):
                    wr.writerow(output[i])
                self.status.configure(text="OUTPUTS UPDATED")

            treev = tree(self, output)
            treev.grid(
                column=1, row=3, columnspan=5, rowspan=10, padx=(90, 0), sticky="e"
            )
        except Exception as e:
            self.status.configure(text="Invalid Input(s)", fg="red")
            print(e)


"""
gamma 99 , 7
thrust desried 55, 16
nozzle exit pressure 19, 22
chamber temperature 0, 21
Chamber Pressure 28, 18

        self.p_1 = p1
        self.t_1 = t1
        self.p_3 = p_3
        self.F = F
        self.k = k
"""
