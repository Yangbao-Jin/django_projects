from math import sqrt

# Initialize a counter for the number of Pythagorean triples
count = 0

# Iterate through all possible values of b
for b in range(1, 28):
    c = sqrt(30**2 + b**2)
    if c.is_integer():
        count += 1
        print(f"Pythagorean triple found: (30, {b}, {int(c)})")

print(f"Total number of Pythagorean triples with one leg 30 and the other leg less than 28: {count}")
