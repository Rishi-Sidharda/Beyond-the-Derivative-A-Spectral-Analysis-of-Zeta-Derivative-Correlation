# this Python script will plot the imaginary value of the zeta function and the derivative of the zeta function

import matplotlib.pyplot as plt
from mpmath import zeta, diff, mp
import numpy as np

# Set the precision for mpmath
mp.dps = 50  # Increase decimal place precision

starting_point = 0
ending_point = 100
density = ending_point * 6  # curve smoothness

im_range = np.linspace(starting_point, ending_point, density)


def compute_zeta_and_derivative(real_part, imag_values):
    zeta_values = []
    derivative_values = []
    for y in imag_values:
        z = real_part + 1j * y
        zeta_val = zeta(z)
        derivative_val = diff(zeta, z)
        zeta_values.append(zeta_val.imag)  # Store the imaginary part of Zeta
        # Store the imaginary part of derivative
        derivative_values.append(derivative_val.imag)
    return zeta_values, derivative_values


# Compute the Zeta function and its derivative along the critical line
zeta_imags, derivative_imags = compute_zeta_and_derivative(0.5, im_range)

# Create the plots
plt.figure(figsize=(10, 6))

# Plot the imaginary parts
plt.plot(im_range, zeta_imags, label='Imaginary Part of Zeta', color='blue')
plt.plot(im_range, derivative_imags,
         label='Imaginary Part of Zeta Derivative', color='red')

# Add titles, labels, and legend
plt.title('Imaginary Parts of Zeta and Its Derivative with time considered')
plt.xlabel('Imaginary Part of Input')
plt.ylabel('Imaginary Output')
plt.legend()

plt.grid(True)
plt.show()
