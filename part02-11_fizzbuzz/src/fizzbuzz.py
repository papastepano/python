# Taking input for an integer number
number = int(input("Number: "))

# Checking divisibility by 3 and 5
if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
elif number % 3 == 0:
    print("Fizz")
elif number % 5 == 0:
    print("Buzz")
else:
    # If the number is not divisible by 3 or 5
    print(number)
