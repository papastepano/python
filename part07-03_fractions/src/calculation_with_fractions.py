# Write your solution here
import fractions

def fractionate(amount: int):
    fractions_list = []
    for i in range(amount):
        fractions_list.append(fractions.Fraction(1,amount))
    return fractions_list


if __name__ == "__main__":
    for p in fractionate(3):
        print(p)

    print()

    print(fractionate(5))