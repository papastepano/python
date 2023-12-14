# Get user input for two numbers and an operation
number1 = int(input("Number 1: "))
number2 = int(input("Number 2: "))
operation = input("Operation: ")

# Check the operation and perform the corresponding calculation
if operation == "add":
    result = number1 + number2
    print(f"{number1} + {number2} = {result}")
elif operation == "multiply":
    result = number1 * number2
    print(f"{number1} * {number2} = {result}")
elif operation == "subtract":
    result = number1 - number2
    print(f"{number1} - {number2} = {result}")
else:
    # If the operation is not add, multiply, or subtract, print nothing
    pass
