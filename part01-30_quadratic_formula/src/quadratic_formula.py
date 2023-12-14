# Write your solution here
# Let's take the square root of math-module in use
from math import sqrt

a = int(input("Value of a: "))
b = int(input("Value of b: "))
c = int(input("Value of c: "))

# Calculate the discriminant
discriminant = b**2 - 4*a*c

# Check if the discriminant is non-negative
if discriminant >= 0:
    # Calculate the two roots using the quadratic formula
    root1 = (-b + sqrt(discriminant)) / (2*a)
    root2 = (-b - sqrt(discriminant)) / (2*a)

    # Print the roots
    print(f"The roots are {root1:.2f} and {root2:.2f}")
else:
    print("The equation has no real roots.")