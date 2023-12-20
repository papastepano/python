# Write your solution here
import math

def hypotenuse(leg1: float, leg2: float):
    # a_plus_b = leg1*leg1 + leg2*leg2
    # c = math.sqrt(a_plus_b)
    c = math.sqrt(leg1**2 + leg2**2)
    return c

if __name__ == "__main__":
    print(hypotenuse(3, 4))
    print(hypotenuse(5, 12))
    print(hypotenuse(1, 1))