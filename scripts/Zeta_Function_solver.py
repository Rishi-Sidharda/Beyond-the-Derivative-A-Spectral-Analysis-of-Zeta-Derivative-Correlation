import mpmath as mp 


mp.mp.dps = 50


def zeta_functional_equation(s):
    pi_term = mp.pi**(s - 1)
    sin_term = mp.sin(mp.pi * s / 2)
    gamma_term = mp.gamma(1 - s)
    zeta_term = mp.zeta(1 - s)

    rhs = 2**s * pi_term * sin_term * gamma_term * zeta_term
    return rhs


def evaluate_lhs(s):
    lhs = mp.zeta(s)
    return lhs


def evaluate_rhs(s):
    rhs = zeta_functional_equation(s)
    return rhs


# Example complex number
# First non-trivial zero
s_val = mp.mpc('0.5', '14.134725141734693790457251983562')

# Evaluate the functional equation
lhs = evaluate_lhs(s_val)
rhs = evaluate_rhs(s_val)

print(mp.nstr(rhs, n=50))
