import math

p1 = float(input("Chamber pressure (PSI): "))
t1 = float(input("Chamber Temperature (kelvin): "))
pe = float(input("Nozzle Exit Pressure (PSI): "))
k = float(input("K (gamma): "))
F = float(input("Thrust desired(N): "))
MM = float(input("Enter Molecular Weight: "))

R = 8.3145 / (MM)
te = t1 * ((pe / p1) ** ((k - 1) / k))
v2 = math.sqrt(
    (((2 * k) / (k - 1)) * (t1 * R))
    * (1 - (((pe / 145) / (p1 / 145)) ** ((k - 1) / k)))
)
vt = math.sqrt(((2 * k) / (k + 1)) * (R * t1))

V1 = (R * t1) / (p1 * 6894.75729)
V2 = V1 * ((p1 / pe) ** (1 / k))
Vt = V1 * (((k + 1) / 2) ** (1 / (k - 1)))

mass_flow = F / v2
A2 = (((mass_flow * V2) / v2) * 10 ** 4) / 6.452
M = v2 / math.sqrt(k * R * te)
At = (((mass_flow * Vt) / vt) * 10 ** 4) / 6.452
ex = A2 / At
r = math.sqrt((At) / math.pi)

t1_rankine = t1 * 1.8
print(" ")
print(
    "*****************************************************************************************"
)
print("Exit Mach Number: " + str(round(M, 5)))
print("Throat Area [in^2]: " + str(round(At, 5)))
print(
    "Throat Radius (Will need to Multiply the Nozzle Contour After Outputted) [in]: "
    + str(round(r, 5))
)
print("Chamber Pressure [Psi]: " + str(round(p1, 5)))
print("Chamber Temperature [R]: " + str(round(t1_rankine, 5)))
print("Gamma: " + str(k))
print("Expansion Ratio: " + str(round(ex, 5)))
