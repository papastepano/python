# Get user input for an integer number
number = int(input("Please type in a number: "))

# Check if the number is less than zero
if number < 0:
    # If it is, print the number multiplied by -1
    print(f"The absolute value of this number is {-number}")
else:
    # If it's not, print the number as is
    print(f"The absolute value of this number is {number}")
