from math import sqrt

def is_pythagorean_triple(a, b):
    # Calculate the square of the hypotenuse
    c_squared = a**2 + b**2
    # Check if the square root of c_squared is an integer
    return sqrt(c_squared).is_integer()

# Example usage:
leg1 = 12
leg2 = 16

if is_pythagorean_triple(leg1, leg2):
    print(f"The sides {leg1} and {leg2} can form a Pythagorean triple.")
else:
    print(f"The sides {leg1} and {leg2} cannot form a Pythagorean triple.")
