import matplotlib.pyplot as plt
from mpmath import zeta, diff, mp
import numpy as np
from scipy.integrate import simps

# Set the precision for mpmath
mp.dps = 50  # Increase decimal place precision

starting_point = 0
ending_point = 100
density = ending_point * 8  # curve smoothness

im_range = np.linspace(starting_point, ending_point, density)


def compute_zeta_and_derivative(real_part, imag_values):
    zeta_values = []
    derivative_values = []
    for y in imag_values:
        z = real_part + 1j * y
        zeta_val = zeta(z)
        derivative_val = diff(zeta, z)
        # Store the imaginary part of Zeta
        zeta_values.append(float(zeta_val.imag))
        # Store the imaginary part of derivative
        derivative_values.append(float(derivative_val.imag))
    return zeta_values, derivative_values


def find_zero_crossings(values, threshold=1e-5):
    zero_crossings = []
    for i in range(1, len(values)):
        if values[i-1] * values[i] < 0 and abs(values[i-1] - values[i]) > threshold:
            zero_crossings.append(i)
    return zero_crossings


# Compute the Zeta function and its derivative along the critical line
zeta_imags, derivative_imags = compute_zeta_and_derivative(0.5, im_range)

# Find zero crossings
zeta_zero_crossings = find_zero_crossings(zeta_imags)
derivative_zero_crossings = find_zero_crossings(derivative_imags)

# Ensure the ranges for integration cover the entire domain
if zeta_zero_crossings[0] != 0:
    zeta_zero_crossings.insert(0, 0)
if zeta_zero_crossings[-1] != len(im_range) - 1:
    zeta_zero_crossings.append(len(im_range) - 1)

# Remove the first area of the zeta function
zeta_zero_crossings = zeta_zero_crossings[1:]
# Keep the first zero crossing of the derivative
derivative_zero_crossings = derivative_zero_crossings

# Calculate the area under the curves between each zero crossing
areas = []
ratios = []
for i in range(1, len(zeta_zero_crossings)):
    start = zeta_zero_crossings[i-1]
    end = zeta_zero_crossings[i]
    area_zeta = simps(np.abs(zeta_imags[start:end]), im_range[start:end])
    if i < len(derivative_zero_crossings):
        start_derivative = derivative_zero_crossings[i-1]
        end_derivative = derivative_zero_crossings[i]
        area_derivative = simps(np.abs(
            derivative_imags[start_derivative:end_derivative]), im_range[start_derivative:end_derivative])
    else:
        area_derivative = 0
    areas.append((i, area_zeta, area_derivative))
    # Calculate the ratio only if both areas are non-zero
    if area_zeta != 0 and area_derivative != 0:
        smaller = min(area_zeta, area_derivative)
        larger = max(area_zeta, area_derivative)
        ratio = smaller / larger
        ratios.append(ratio)

# Calculate the average ratio
average_ratio = np.mean(ratios)
print(f'Average Ratio: {average_ratio}')

# Calculate the similarity of each ratio to the average ratio
similarities = []
for ratio in ratios:
    similarity = (1 - abs(ratio - average_ratio) /
                  max(ratio, average_ratio)) * 100
    similarities.append(similarity)

# Calculate the overall similarity
overall_similarity = np.mean(similarities)

# Print the overall similarity
print(f'Overall Similarity: {overall_similarity}%')

# Save the areas, ratios, and similarities to a text file
with open("Double_Function_areas_with_similarity.txt", "w") as f:
    for index, area_zeta, area_derivative in areas:
        f.write(f"Index: {index}, Area under Zeta: {
                area_zeta}, Area under Derivative: {area_derivative}\n")
    f.write("\nRatios:\n")
    for index, ratio in enumerate(ratios, start=1):
        f.write(f"Index: {index}, Ratio: {ratio}\n")
    f.write("\nSimilarities of each ratio to the average ratio:\n")
    for index, similarity in enumerate(similarities, start=1):
        f.write(f"Index: {index}, Similarity: {similarity}\n")

# Create the plots
plt.figure(figsize=(10, 6))

# Plot the imaginary parts
plt.plot(im_range, zeta_imags, label='Imaginary Part of Zeta', color='blue')
plt.plot(im_range, derivative_imags,
         label='Imaginary Part of Zeta Derivative', color='red')

# Shade the areas being calculated for zeta function
for i in range(2, len(zeta_zero_crossings)):
    start = zeta_zero_crossings[i-1]
    end = zeta_zero_crossings[i]
    plt.fill_between(im_range[start:end],
                     zeta_imags[start:end], color='blue', alpha=0.1)

# Shade the areas being calculated for zeta derivative
for i in range(1, len(derivative_zero_crossings)):
    start = derivative_zero_crossings[i-1]
    end = derivative_zero_crossings[i]
    plt.fill_between(
        im_range[start:end], derivative_imags[start:end], color='red', alpha=0.1)

# Add titles, labels, and legend
plt.title('Imaginary Parts of Zeta and Its Derivative with Shaded Areas')
plt.xlabel('Imaginary Part of Input')
plt.ylabel('Imaginary Output')
plt.legend()

plt.grid(True)
plt.show()
