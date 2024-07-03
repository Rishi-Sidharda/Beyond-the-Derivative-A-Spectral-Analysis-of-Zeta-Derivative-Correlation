import matplotlib.pyplot as plt
from mpmath import zeta, mp
import numpy as np

# Set the precision for mpmath
mp.dps = 50  # Increase decimal place precision
starting_point = 0
ending_point = 100
density = ending_point * 6  # curve smoothness

# Define the range for the imaginary part of the input
im_range = np.linspace(starting_point, ending_point, density)

# Function to calculate Zeta


def compute_zeta(real_part, imag_values):
    zeta_values = []
    for y in imag_values:
        z = real_part + 1j * y
        zeta_val = zeta(z)
        zeta_values.append(zeta_val.imag)  # Store the imaginary part of Zeta
    return zeta_values


# Compute the Zeta function along the critical line
zeta_imags = compute_zeta(0.5, im_range)

# Create the plot
plt.figure(figsize=(10, 6))

# Plot the imaginary parts
plt.plot(im_range, zeta_imags, label='Imaginary Part of Zeta', color='blue')

# Add titles, labels, and legend
plt.title('Imaginary Part of the Zeta Function with Time')
plt.xlabel('Imaginary Part of Input')
plt.ylabel('Imaginary Output')
plt.legend()

plt.grid(True)
plt.show()
