import matplotlib.pyplot as plt
from mpmath import zeta, diff, mp
import numpy as np

# Set the precision for mpmath
mp.dps = 50  # Increase decimal place precision

# Define the range for the imaginary part of the input

starting_point = 0
ending_point = 100
density = ending_point * 6  # curve smoothness

im_range = np.linspace(starting_point, ending_point, density)
# Function to calculate the derivative of Zeta


def compute_derivative(real_part, imag_values):
    derivative_values = []
    for y in imag_values:
        z = real_part + 1j * y
        derivative_val = diff(zeta, z)
        # Store the imaginary part of the derivative
        derivative_values.append(derivative_val.imag)
    return derivative_values


# Compute the derivative of the Zeta function along the critical line
derivative_imags = compute_derivative(0.5, im_range)

# Create the plot
plt.figure(figsize=(10, 6))

# Plot the imaginary parts of the derivative
plt.plot(im_range, derivative_imags,
         label='Imaginary Part of Zeta Derivative', color='red')

# Add titles, labels, and legend
plt.title('Imaginary Part of the Zeta Function Derivative')
plt.xlabel('Imaginary Part of Input')
plt.ylabel('Imaginary Output')
plt.legend()

plt.grid(True)
plt.show()
