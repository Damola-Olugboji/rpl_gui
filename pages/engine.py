import tkinter as tk
from widgets.entry_unit import entry_with_unit as ewu
from widgets.checkbox import checkbox as chk
from calculations.tree_results import tree
import math, csv


class engine_calculations(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)
        self.grid_rowconfigure(4, weight=1)
        self.grid_rowconfigure(5, weight=1)
        self.grid_rowconfigure(6, weight=1)
        self.grid_rowconfigure(7, weight=1)
        self.grid_rowconfigure(8, weight=1)
        self.grid_rowconfigure(9, weight=1)
        self.grid_rowconfigure(10, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.import_from_propellant = tk.Button(self, text = "Import Characteristics", fg = 'black',width = 30, font=("Garamond", 14), command = self.import_from_prop)        
        self.enter_manually = tk.Button(self, text ="Clear", fg = 'black', width = 30,font=("Garamond", 14), command = self.clear )
        self.import_from_propellant.grid(column = 0, row = 0, sticky = 'w', pady = (0,10))
        self.enter_manually.grid(column = 0, row = 1, sticky = 'w',pady = (10,10))
        
        #Inputs
        self.p1 = ewu(self, "Chamber Pressure: ", ["PSI"])
        self.p1.grid(column=0, row=2, pady=5, sticky="w")
        self.t1 = ewu(self, "Chamber Temperature: ", ["K", "R", "C", "F"])
        self.t1.grid(column=0, row=3, sticky="w", pady = 5)
        self.pe = ewu(self, "Ambient Pressure: ", ["PSI"])
        self.pe.grid(column=0, row=4, pady=5, sticky="w")
        self.F = ewu(self, "Thrust Desired: ", ["N"])
        self.F.grid(column=0, row=5, sticky="w", pady = 8)
        self.k = ewu(self, "Gamma: ", [""])
        self.k.grid(column=0, row=6, padx=0, pady=5, sticky="w")
        self.i_t = ewu(self, "Total Impulse: ", ["N-s"])
        self.i_t.grid(column =0, row = 7, sticky = 'w', pady = 5)
        self.configure(bg="#222831")
        self.MM = ewu(self, "Molecular Weight: ", [""])
        self.MM.grid(column = 0, row = 8, sticky = 'w', pady = 5)
        self.note = tk.Label(self, text = "Note: Total Impulse Input is optional", fg = 'white',bg = '#222831', font = ("Franklin Gothic Medium", 12))
        self.note.grid(column = 0, row = 9, sticky = 'w', pady = 5)
        self.display_results = tk.Button(
            self,
            text="Display Results",
            bg="#f1eff2",
            fg="black",
            width=20,
            font=("Garamond", 18),
            command=lambda: self.calculate(
                self.p1, self.t1, self.pe, self.F, self.k, self.i_t, self.MM
            )
            # add parameters
        )
        self.display_results.grid(column=1, row=0, padx=(100, 0))   
        self.status = tk.Label(
            self,
            text="OUTPUTS NOT UPDATED",
            font=("Garamond", 14),
            fg="white",
            bg="#222831",
        )
        self.status.grid(column=1, row=1, padx=(100, 0))
        self.check = tk.Label(self,text = "", fg = 'white', bg = '#222831', font = ("Franklin Gothic Medium", 15))
        self.check.grid(column =0, row = 10, sticky = 'w')
    def clear(self):
        self.p1.clear()
        self.t1.clear()
        self.pe.clear()
        self.F.clear()
        self.k.clear()
        self.i_t.clear()
        self.check.configure(text = "")
    def import_from_prop(self):
        from pages.propellant import outsidep
        if outsidep == 0:
            self.check.configure(text = "Propellant Information Unavailable", fg = 'red')
            self.p1.clear()
            self.t1.clear()
            self.pe.clear()
            self.F.clear()
            self.k.clear()
            self.i_t.clear()
            self.MM.clear()
        else:
            self.p1.clear()
            self.t1.clear()
            self.pe.clear()
            self.F.clear()
            self.k.clear()
            self.i_t.clear()
            self.MM.clear()
            self.p1.default(round(outsidep.properties[0].P*14.696,3))
            self.pe.default(round(outsidep.properties[2].P*14.696,3))
            self.t1.default(round(outsidep.properties[0].T,3))
            self.k.default(round(outsidep.properties[0].Cp/outsidep.properties[0].Cv,3))
            #self.MM.default(round(,3))
    def calculate(self, p_1, t_1, p_3, F, k, i_t, MM):
        try:
            p1 = p_1.val()  # convert all MPa
            t1 = t_1.val()
            p3 = p_3.val()
            it = i_t.val()
            MM = MM.val()
            F = F.val()  # don't need units, use N
            k = k.val()  # don't need units
            R = 8.3145 / (MM/ 1000)  # need molecular weight input for R value
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
                column=1, row=2, columnspan=5, rowspan=6, padx=(90, 0), sticky="n"
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
        
        self.optional = tk.Label(
            self,
            text="Optional Parameters",
            fg="#1EA51D",
            bg="#222831",
            font=("Franklin Gothic Demi", 15),
        )
        self.optional.grid(column=0, row=7, pady=(12, 0), sticky="w")
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
        
        self.graph1.grid(column=0, row=9, padx=0, sticky="w")
        self.graph2.grid(column=0, row=10, padx=0, sticky="w")
        self.graph3.grid(column=0, row=11, padx=0, sticky="w")
        self.i_t.grid(column=0, row=8, sticky="w", padx=(0, 0), pady=5
"""
