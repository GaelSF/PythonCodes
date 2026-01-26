from math import sqrt

m = 9.11e-31 # electron mass
hbar = 6.58e-16 # Planck's constant (eV.s)
E = 10.0 # Energy (eV)
V = 9.0 # Energy (eV)

# Compute wave numbers
k1 = sqrt(2.0*m*E)/hbar
k2 = sqrt(2.0*m*(E-V))/hbar

# Transmission coefficient
T = 4.0*k1*k2/((k1+k2)**2)

# Reflection coefficient
R = ((k1-k2)/(k1+k2))**2

print(f"Transmission = {T:.3f}")
print(f"Reflection = {R:.3f}")

# Vertical blank
print()

print(f"Sum of probabilities = {T+R:.3f}")
