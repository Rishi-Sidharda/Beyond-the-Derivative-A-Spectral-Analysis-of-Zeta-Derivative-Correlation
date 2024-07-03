import matplotlib.pyplot as plt
from mpmath import zeta, mp
import numpy as np

# Set the precision for mpmath
mp.dps = 50  # Increase decimal place precision
starting_point = 0
ending_point = 100
density = ending_point * 8  # curve smoothness

# Define the range for the imaginary part of the input
im_range = np.linspace(starting_point, ending_point, density)

# Function to calculate Zeta


def compute_zeta(real_part, imag_values):
    zeta_values = []
    for y in imag_values:
        z = real_part + 1j * y
        zeta_val = zeta(z)
        # Store the imaginary part of Zeta as a float
        zeta_values.append(float(zeta_val.imag))
    return zeta_values


# Compute the Zeta function along the critical line
zeta_imags = compute_zeta(0.5, im_range)

# Find the first zero crossing
first_zero_index = next(i for i, val in enumerate(zeta_imags) if val > 0)
first_zero_im_value = im_range[first_zero_index]

# Create the plot
plt.figure(figsize=(10, 6))

# Plot the imaginary parts
plt.plot(im_range, zeta_imags, label='Imaginary Part of Zeta', color='blue')

# Shade positive areas
plt.fill_between(im_range, zeta_imags, where=(
    np.array(zeta_imags) > 0), color='green', alpha=0.3)

# Shade negative areas
plt.fill_between(im_range, zeta_imags, where=(
    np.array(zeta_imags) < 0), color='red', alpha=0.3)

# Add titles, labels, and legend
plt.title('Imaginary Part of the Zeta Function with Time')
plt.xlabel('Imaginary Part of Input')
plt.ylabel('Imaginary Output')
plt.legend()

# Highlight the unshaded area up to the first zero
plt.fill_between(im_range[:first_zero_index],
                 zeta_imags[:first_zero_index], color='white', alpha=1)

plt.grid(True)
plt.show()
