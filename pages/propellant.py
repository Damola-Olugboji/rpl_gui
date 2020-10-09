import tkinter as tk
import pypropep as ppp
from tkinter import ttk
import os, sys, math
from data.propellant_data import propellant_data
from widgets.autoComboBox import AutocompleteCombobox

"""
Thermodynamic Performance and Chemical Equilibrium Composition Calculations
based on Nasa publication by Sanford Gordon and Bonnie J. McBride
https://www.grc.nasa.gov/www/CEAWeb/RP-1311.pdf
"""
outsidep = 0

class propellant_calculations(tk.Frame):
    prop_variable = 0 #initialization of a variable that will eventually contian pypropep propellant data
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.configure(bg="#222831")
        # self.frame = tk.Frame(self)
        # self.frame.grid(column=0, row=0, sticky="nesw")
        self.label = tk.Label(
            self,
            text="Propellant Names",
            fg="white",
            bg="#222831",
            font=("Garamond", 15),
        )
        self.label.grid(column=0, row=0)
        self.weight_label = tk.Label(
            self, text="Weight(gr)", fg="white", bg="#222831", font=("Garamond", 15)
        )
        self.weight_label.grid(column=1, row=0)
        w, h = 2, 10
        self.prop = [[0 for x in range(w)] for y in range(h)]
        for i in range(0, h):
            self.prop[i][0] = AutocompleteCombobox(self)
            self.prop[i][0].set_completion_list(propellant_data)
            self.prop[i][0].configure(width="40", font=("Franklin Gothic Medium", 12))
            self.prop[i][0].grid(column=0, row=i + 1, pady=5)
            self.prop[0][0].focus_set()
            self.prop[i][1] = tk.Entry(
                self, width=10, font=("Franklin Gothic Medium", 12)
            )
            self.prop[i][1].grid(column=1, row=i + 1, padx=(10, 0))

        # operating parameters section
        self.operating_parameters_label = tk.Label(
            self,
            bg="#222831",
            fg="white",
            text="Operating Conditions",
            font=("Garamond", 15),
        )
        self.operating_parameters_label.grid(column=2, row=0, sticky="w", padx=(65, 0))
        
        self.operating_temp_label = tk.Label(
            self,
            text="Ingredient Temperature (K): ",
            font=("Garamond", 15),
            fg="white",
            bg="#222831",
        )
        self.operating_temp = tk.Entry(self,font=("Franklin Gothic Medium", 12),)
        self.operating_chamber_pressure_label = tk.Label(
            self,
            text="Chamber Pressure (PSI): ",
            font=("Garamond", 15),
            fg="white",
            bg="#222831",
        )
        self.operating_temp.insert(0,"298")
        self.operating_temp.config(state = 'disabled')
        self.operating_chamber_pressure = tk.Entry(self, font=("Franklin Gothic Medium", 12))
        self.operating_chamber_pressure.insert(0, "1000")
        self.operating_exhaust_pressure_label = tk.Label(
            self,
            text="Exhaust Pressure (PSI): ",
            font=("Garamond", 15),
            fg="white",
            bg="#222831",
        )
        self.operating_exhaust_pressure = tk.Entry(self,font=("Franklin Gothic Medium", 12))
        self.operating_exhaust_pressure.insert(0, "14.7")
        self.operating_temp.grid(column=3, row=1, padx=(30, 0), sticky="w")
        self.operating_temp_label.grid(column=2, row=1, padx=(65, 0), sticky="w")
        self.operating_chamber_pressure_label.grid(
            column=2, row=2, padx=(65, 0), sticky="w"
        )
        self.operating_chamber_pressure.grid(column=3, row=2, padx=(30, 0), sticky="w")
        self.operating_exhaust_pressure_label.grid(
            column=2, row=3, padx=(65, 0), sticky="w"
        )
        self.operating_exhaust_pressure.grid(column=3, row=3, padx=(30, 0), sticky="w")
        
        self.validation_label = tk.Label(self, text = "",bg = '#222831', font = ("Garamond", 16))
        self.validation_label.grid(column = 2, row = 5, columnspan = 2, sticky = 'n', rowspan = 2, padx = (20,0))
        
        self.reset_button = tk.Button(self, text = "reset", font = ("Garamond", 18), width = 15, fg = 'white', bg = 'red', command = lambda: self.clear(self.prop))
        self.calculate_button = tk.Button(
            self,
            text="calculate",
            font=("Garamond", 18),
            width=10,
            fg="black",
            bg="#f1eff2",command = lambda: self.validation(self.prop, self.operating_chamber_pressure.get(), self.operating_exhaust_pressure.get())
        )
        self.calculate_button.grid(column=2, row=12, sticky="n", rowspan=2, )
        self.display_button = tk.Button(
            self,
            text="Display \nResults",
            font=("Garamond", 18),
            width=10,
            fg="black",
            bg="#f1eff2", command = self.results
        )
        self.display_button.grid(column=3, row=12, sticky="w", rowspan=2)
        self.display_button.config(state = 'disabled')


    def validation(self,prop, p1, pe):
        flag = 0
        #check if there are entries in both the propellant selection and weight selection
        #check if propellant entry is valid, check if weight entry is float 
        self.prop = prop
        self.p1 = p1
        self.pe = pe
        self.prop_final = [[0 for x in range(0)] for y in range(0)]

        for i in range(0, len(self.prop)):
            if prop[i][0].get() != "" and prop[i][1].get() != "":
                if prop[i][0].get() in propellant_data and self.will_it_float(prop[i][1].get()):
                    self.prop_final.append([prop[i][0].get(), prop[i][1].get()])
                    if self.will_it_float(self.p1) and self.will_it_float(self.pe):
                        flag = 1
                    elif not(self.will_it_float(p1)) or not (self.will_it_float(pe)):
                        flag = 2
                elif not(prop[i][0].get() in propellant_data) or self.will_it_float(prop[i][1].get()) == False:
                    flag = -1
                    break
            elif prop[i][0].get() == "" and prop[i][0].get() == "":
                continue
            elif prop[i][0].get() == "" or prop[i][1].get() == "":
                flag = 0
                break
            
        if flag == 1:
            print("sucessful entry")
            self.calculate(self.prop_final, float(self.p1),float(self.pe))
        if flag == -1:
            self.validation_label.configure(text = "Propellant Inputs must be selected from drop down \n Weight inputs must be positive float values", fg = 'white', bg = 'red')
        if flag == 0:
            self.validation_label.configure(text = "Inputs are missing", fg= 'white', bg = 'red')
        if flag == 2:
            self.validation_label.configure(text = "Re-check Operating Parameters", fg = 'white', bg = 'red')
                
    def calculate(self, prop, p1, pe):
        try: 
            self.calc_prop = prop
            self.p1 = p1/14.696 #converting psi to atm
            self.pe = pe/14.696
            ppp.init()
            self.p = ppp.FrozenPerformance()
            self.calc_prop_var = [0]*len(self.calc_prop)
            list_tuple = []
            self.prop_weight = 0
            self.propellant_list = []
            for i in range(0, len(self.calc_prop)):
                self.propellant_list.append(self.calc_prop[i][0])
                self.calc_prop_var[i] = ppp.PROPELLANTS[self.calc_prop[i][0]]
                self.prop_weight += float(self.calc_prop[i][1])
                list_tuple.append((self.calc_prop_var[i], float(self.calc_prop[i][1])))
            self.p.add_propellants_by_mass(list_tuple)    
            self.p.set_state(P = float(self.p1), Pe = float(self.pe))
            self.calculate_button.config(state = 'disabled')
            self.display_button.config(state = 'active')
            self.reset_button.grid(column = 2, row = 7, columnspan = 2, rowspan = 2, sticky = 'n')
            self.validation_label.configure(text = "Total Weight: " + str(self.prop_weight), fg = 'white', bg = "#222831")
            #self.validation_label.configure(text = "Sucess :)", bg = 'green', fg = 'white', font = ("Garamond", 20))
            propellant_calculations.prop_variable = self.p
            global outsidep
            outsidep = self.p
            

            
        except Exception as e:
            print("ERROR")
            self.validation_label.configure(text = "System Error :/", fg = 'white', bg = 'red')
            
        
            
    def results(self):
        tl_results = tk.Toplevel(self,)
        tl_results.geometry('1100x550')
        tl_results.title("Propellant Combustion Charactersitics")
        tl_results.grid()
        
        for i in range(0, 3):
            if i == 0:
                location = "========= Chamber =========:"
            if i == 1:
                location = "========= Throat =========:"
            if i == 2:
                location = "========= Exit =========:"
            self.location_label = tk.Label(tl_results, fg = 'black', text = location, font = ('Garamond', 14))
            self.temperature_label = tk.Label(tl_results, fg = 'black',  text = "Temperature: "+ str(round(propellant_calculations.prop_variable.properties[i].T,5)) +" K", font = ('Garamond', 12))
            self.pressure_label = tk.Label(tl_results, fg = 'black',  text = "Pressure: "+str(round(propellant_calculations.prop_variable.properties[i].P,5)) + " atm", font = ('Garamond', 12))
            self.cp_label = tk.Label(tl_results, fg = 'black', text ="Cp: "+ str(round(propellant_calculations.prop_variable.properties[i].Cp,5)), font = ('Garamond', 12))
            self.cv_label = tk.Label(tl_results, fg = 'black', text ="Cv: "+str(round(propellant_calculations.prop_variable.properties[i].Cv,5)), font = ('Garamond', 12))
            self.gamma_label = tk.Label(tl_results, fg = 'black', text = "Gamma: "+str(round(propellant_calculations.prop_variable.properties[i].Cp/propellant_calculations.prop_variable.properties[i].Cv,5)), font = ('Garamond', 12))
            self.MM_label = tk.Label(tl_results, fg = 'black', text = "Molar Mass: "+str(round(propellant_calculations.prop_variable.properties[i].M,5)), font = ('Garamond', 12))
                                     
            self.location_label.grid(column = i, row = 0, padx = (15,0), sticky = 'w')
            self.temperature_label.grid(column = i, row = 1, padx = (15,0), sticky = 'w')
            self.pressure_label.grid(column = i, row = 2, padx = (15,0), sticky = 'w')
            self.cp_label.grid(column = i, row = 3, padx = (15,0), sticky = 'w')
            self.cv_label.grid(column = i, row = 4, padx = (15,0), sticky = 'w')
            self.gamma_label.grid(column = i, row = 5, padx = (15,0), sticky = 'w')
            self.MM_label.grid(column = i, row = 6, padx = (15,0), sticky = 'w')
            
        self.performance_label = tk.Label(tl_results,text = "========= Perfromance =========:", font = ("Garamond", 14))
        self.isp_label = tk.Label(tl_results, text = "Specific Impulse (m/s): "+ str(round(propellant_calculations.prop_variable.performance.Isp,5)), font = ('Garamond', 12))
        self.cstar_label = tk.Label(tl_results,text = "C* (m/s): " + str(round(propellant_calculations.prop_variable.performance.cstar,5)), fg = 'black', font = ('Garamond', 12))
        self.ispg_label = tk.Label(tl_results,text = "Specific Impulse/gravity (s): " + str(round(propellant_calculations.prop_variable.performance.Isp/9.80665,5)), fg = 'black', font = ('Garamond', 12))
        self.cf = tk.Label(tl_results,text = "Thrust Coefficient: " + str(round(propellant_calculations.prop_variable.performance.cf,5)), fg = 'black', font = ('Garamond', 12))
        
        self.performance_label.grid(column = 0, row = 7, pady = (10,0), padx = (15,0))
        self.isp_label.grid(column = 0, row = 8, padx = (15,0), sticky = 'w')
        self.cstar_label.grid(column = 0, row = 9, padx = (15,0), sticky = 'w')
        self.ispg_label.grid(column = 0, row = 10, padx = (15,0), sticky = 'w')
        self.cf.grid(column = 0, row = 11, padx = (15,0), sticky = 'w')
        
        self.propellant_label = tk.Label(tl_results, text = "========= Propellants =========", font = ("Garamond", 14))
        self.propellant_label.grid(column = 1, row = 7, sticky = 'w')
        for i in range (0, len(self.propellant_list)):
            self.list_propellant = tk.Label(tl_results, text = self.propellant_list[i], font = ("Garamond", 12))
            self.list_propellant.grid(column = 1, row = 7+i, sticky = 'w')
            

        
    #helper functions
        
    def will_it_float(self, val):
        try:
            float(val)
            return float(val)>0
        except ValueError:
            return False
    
    def clear(self, prop):
        self.prop = prop
        for i in range(0, len(self.prop)):
            self.prop[i][0].delete(0, 'end')
            self.prop[i][1].delete(0, 'end')
            self.reset_button.grid_forget()
            self.calculate_button.config(state = 'active')
            self.display_button.config(state = 'disabled')
            self.validation_label.configure(text = "")
            global outsidep
            outsidep = 0
            #self.validation_label.grid_remove()
    
























