import matplotlib.pyplot as plt
from mpmath import zeta, mp

# Set the precision (number of decimal places)
mp.dps = 50

# Generate points along the critical line (s = 0.5 + it)
t_values = [t * 0.01 for t in range(1, 3000)]
zeta_values = [zeta(0.5 + 1j*t) for t in t_values]

# Separate the real and imaginary parts for plotting
real_parts = [zeta.real for zeta in zeta_values]
imaginary_parts = [zeta.imag for zeta in zeta_values]

# Plot the complex values on the Argand diagram
plt.figure(figsize=(8, 8))
plt.plot(real_parts, imaginary_parts, color='red')
plt.xlabel('Re ζ(0.5 + it)')
plt.ylabel('Im ζ(0.5 + it)')
plt.title('Polar graph of Riemann zeta(0.5 + it)')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.show()
