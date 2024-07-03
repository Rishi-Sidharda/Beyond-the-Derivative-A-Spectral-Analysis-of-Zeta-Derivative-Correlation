import matplotlib.pyplot as plt

# Given points
points_set2 = [(100, 43.1837392168981427), (1000,
                                            31.1962963190218119388), (2000, 30.05892116216378348897325)]
x_values_set2, y_values_set2 = zip(*points_set2)

# Plotting
plt.figure(figsize=(10, 6))

# Plotting first set of points

# Plotting second set of points
plt.plot(x_values_set2, y_values_set2, marker='o', label='Second Function')

plt.title('Plot of Given Points')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.grid(True)
plt.show()
