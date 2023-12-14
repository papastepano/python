# Taking input for the first number
num1 = int(input("Please type in the first number: "))

# Taking input for the second number
num2 = int(input("Please type in another number: "))

# Comparing the numbers
if num1 > num2:
    print("The greater number was:", num1)
elif num1 < num2:
    print("The greater number was:", num2)
else:
    print("The numbers are equal!")
