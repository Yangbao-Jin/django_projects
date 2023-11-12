from math import sqrt

# Initialize a list to hold the Pythagorean triples
pythagorean_triples = []

# Iterate through all possible values of b
for b in range(1, 30):  # b is less than 30
    c = sqrt(12**2 + b**2)
    if c.is_integer():
        pythagorean_triples.append((12, b, int(c)))

# Print out the found Pythagorean triples and their count
for triple in pythagorean_triples:
    print(f"Pythagorean triple: {triple}")

print(f"Total number of Pythagorean triples: {len(pythagorean_triples)}")
