import matplotlib.pyplot as plt
from mpmath import zeta, mp
import numpy as np
from scipy.integrate import simps
import pandas as pd

# Set the precision for mpmath
mp.dps = 50  # Increase decimal place precision
starting_point = 0
ending_point = 2000
density = ending_point * 8  # curve smoothness

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

# Find the indices of the zero crossings
zero_crossings = np.where(np.diff(np.sign(zeta_imags)))[0]

# Calculate the area between each zero crossing
areas = []
for i in range(len(zero_crossings) - 1):
    x1 = im_range[zero_crossings[i]:zero_crossings[i + 1]]
    y1 = zeta_imags[zero_crossings[i]:zero_crossings[i + 1]]
    area = simps(np.abs(y1), x1)
    areas.append(area)

# Group areas into sets of two starting from the first index
grouped_areas = [areas[i:i + 2] for i in range(1, len(areas), 2)]

# Calculate the ratios for each set
ratios = []
for pair in grouped_areas:
    if len(pair) == 2 and pair[1] != 0:
        ratio = pair[0] / pair[1]
        ratios.append(ratio)
    else:
        # In case of an odd number of areas or division by zero
        ratios.append(None)

# Filter out None values from ratios and corresponding grouped areas
filtered_ratios = [r for r in ratios if r is not None]
filtered_grouped_areas = [grouped_areas[i]
                          for i in range(len(grouped_areas)) if ratios[i] is not None]

# Calculate the average ratio
average_ratio = np.mean(filtered_ratios)

# Calculate the similarity of each ratio to the average ratio
similarities = []
for ratio in filtered_ratios:
    similarity = (1 - abs(ratio - average_ratio) /
                  max(ratio, average_ratio)) * 100
    similarities.append(similarity)

# Calculate the overall similarity
overall_similarity = np.mean(similarities)

# Print the overall similarity
print(f'Overall Similarity: {overall_similarity}%')

# Write the grouped areas and their ratios to a text file
with open('Zeta_functio_integral_areas_with_ratios.txt', 'w') as f:
    f.write('Area Groups and Ratios\n')
    f.write('=======================\n')
    for i, (group, ratio) in enumerate(zip(filtered_grouped_areas, filtered_ratios)):
        f.write(f'Group {i+1}: {group}, Ratio: {ratio}\n')

# Create the plot
plt.figure(figsize=(10, 6))

# Plot the imaginary parts
plt.plot(im_range, zeta_imags, label='Imaginary Part of Zeta', color='blue')

# Add titles, labels, and legend
plt.title('Imaginary Part of the Zeta Function')
plt.xlabel('Imaginary Part of Input')
plt.ylabel('Imaginary Output')
plt.legend()

plt.grid(True)
plt.show()
