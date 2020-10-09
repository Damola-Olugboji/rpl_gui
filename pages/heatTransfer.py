import tkinter as tk
from widgets.entry_nounit import entry_nounit as enu

class heatTransferHub(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.configure(bg = "#222831")
        self.toggle1 = tk.Button(self, text = "Bartz Heat ",font=("Garamond", 15), command=lambda *args: self.toggle(str(1)))
        self.toggle2 = tk.Button(self, text = "Viscosity Calculator", font=("Garamond", 15),command=lambda *args: self.toggle(str(2)))
        self.toggle1.grid(column = 0, row = 1)
        self.toggle2.grid(column = 1, row = 1, padx = 30, pady = 10)
        self.temp = bartz(self)
        self.temp.grid(column = 0, row = 2, columnspan = 20)
    def toggle(self, var):
        if var == "1":
            self.temp.grid_forget()
            self.temp = bartz(self)
            self.temp.grid(column = 0, row = 2, columnspan = 20)
        elif var == "2": 
            self.temp.grid_forget()
            self.temp = viscosityCalculator(self)
            self.temp.grid(column = 0, row = 2, columnspan = 20)




class bartz(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self,parent)
        self.configure(bg="#222831")

        self.parent = parent
        self.label = tk.Label(self, text ="Bartz Heat Transfer", fg = 'white',font=("Garamond", 20), bg = "#222831")
        self.label.grid(column = 0, row = 0, sticky = 'w', pady = (10, 0))

        self.t0 = enu(self, "Stagnation Temperature(K): ")
        self.t0.grid(column = 0, row = 1, sticky = 'w')
        self.p0 = enu(self, "Stagnation Pressure(MPa): ")
        self.p0.grid(column = 0, row = 2, sticky = 'w')
        self.tr = enu(self, "Throat Radius(M): ")
        self.tr.grid(column = 0,row =3, sticky = 'w')
        self.k = enu(self, "Gamma: ")
        self.k.grid(column = 0 ,row = 4, sticky = 'w')
        self.t_w = enu(self, "Real Wall Temperture(K): ")
        self.t_w.grid(column = 0, row =5, sticky = 'w')
        self.c_p = enu(self, "Specific Heat of Exhaust: ")
        self.c_p.grid(column = 0, row = 6, sticky = 'w')
        self.recoveryFactor = enu(self, "Recovery Factor: ")
        self.recoveryFactor.grid(column = 0, row = 7, sticky = 'w')
        self.mu_0 = enu(self, "W value")
        self.mu_0.grid(column = 0, row = 8, sticky = 'w')
        self.cstar = enu(self, "Characteristic Velocity(m/s): ")
        self.cstar.grid(column = 0, row = 9, sticky = 'w')
        #self.Pr_o = (4*k.val())/((9*k.val())-5) #stagnant prental(maybe) number 
        self.td = self.tr.val() * 2



        
class viscosityCalculator(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self,parent)
        self.parent = parent
        self.configure(bg="#222831")
        self.label = tk.Label(self, text ="Viscosity Calculator", fg = 'red',font=("Garamond", 25))
        self.label.grid(column = 0, row = 0)
