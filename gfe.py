import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

def G_solid(T):
    return -7976.15 + 137.093038 * T - 24.3671976 * T * np.log(T) - 1.884662E-3 * T**2 - 0.877664E-6 * T**3
def G_liquid(T):
    return -795.996 + 177.430178 * T - 31.748192 * T * np.log(T)


T_range = np.linspace(300, 1500, 500) 

G_s = G_solid(T_range)
G_l = G_liquid(T_range)

def find_melting_temp(T):
    return G_solid(T) - G_liquid(T)

T_melting = fsolve(find_melting_temp, x0=933.47)[0]

plt.figure(figsize=(8, 6))
plt.plot(T_range, G_s, label='Solid Al (FCC)', color='blue')
plt.plot(T_range, G_l, label='Liquid Al', color='red')
plt.axvline(T_melting, color='black', linestyle='--', label=f'Melting T ≈ {T_melting:.2f} K')
plt.xlabel('Temperature (K)')
plt.ylabel('Gibbs Free Energy (J/mol)')
plt.title('Gibbs Free Energy vs Temperature for Aluminum (Al)')
plt.legend()
plt.grid()
plt.show()

print(f"Estimated melting temperature of Aluminum (Al): {T_melting:.2f} K")
