# Write your solution here
import random

def lottery_numbers(amount: int, lower: int, upper: int):
    numbers = []
    while len(numbers) < amount:
        number = random.randint(lower, upper)
        if number not in numbers:
            numbers.append(number)
    return sorted(numbers)

if __name__ == "__main__":
    for number in lottery_numbers(1, 1, 10):
        print(number)