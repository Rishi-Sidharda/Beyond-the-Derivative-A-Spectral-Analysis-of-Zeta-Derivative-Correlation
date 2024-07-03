import mpmath as mp

# Set the precision (number of decimal places)
mp.mp.dps = 50  # Adjust this value based on the desired precision level

# Define the derivative of the zeta function


def zeta_derivative(s):
    return mp.zeta(s, derivative=1)

# Define the functional equation for the derivative of the zeta function
# This is a direct derivative of the functional equation used for zeta itself


def derivative_functional_equation(s):
    pi_term = mp.pi**(s - 1)
    sin_term = mp.sin(mp.pi * s / 2)
    gamma_term = mp.gamma(1 - s)
    zeta_derivative_term = mp.zeta(1 - s, derivative=1)

    # Components that require differentiation
    derivative_pi_term = mp.diff(lambda x: mp.pi**x, s - 1)
    derivative_sin_term = mp.diff(lambda x: mp.sin(mp.pi * x / 2), s)
    derivative_gamma_term = mp.diff(lambda x: mp.gamma(1 - x), s)

    # Calculate the right-hand side of the derivative functional equation
    rhs_derivative = 2**s * (derivative_pi_term * sin_term * gamma_term * mp.zeta(1 - s) +
                             pi_term * derivative_sin_term * gamma_term * mp.zeta(1 - s) +
                             pi_term * sin_term * derivative_gamma_term * mp.zeta(1 - s) +
                             pi_term * sin_term * gamma_term * zeta_derivative_term)
    return rhs_derivative

# Function to evaluate the zeta function derivative and compare


def evaluate_and_compare_derivative(s):
    # Evaluate the derivative of the zeta function at s
    derivative_lhs = zeta_derivative(s)

    # Evaluate the functional equation's RHS for the derivative
    derivative_rhs = derivative_functional_equation(s)

    # Return both derivatives for comparison
    return derivative_lhs, derivative_rhs


# Example complex number
# First non-trivial zero
s_val = mp.mpc('-2.7172628292045741015705806616765284124247518539175', '0.0')

# Evaluate the functional equation for the derivative
derivative_lhs, derivative_rhs = evaluate_and_compare_derivative(s_val)

# Print the results with high precision
print("Zeta'(s) =")
print(mp.nstr(derivative_lhs, n=50))
print("\nFunctional Equation for Zeta' RHS =")
print(mp.nstr(derivative_rhs, n=50))
