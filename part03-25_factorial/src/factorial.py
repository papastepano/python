# Write your solution here
while True:
    user_input = int(input("Please type in a number: "))
    factorial = 1

    if user_input <= 0:
        print("Thanks and bye!")
        break
    else:
        result  = 1
        while factorial <= user_input:
            result  *= factorial
            factorial += 1
        print(f"The factorial of the number {user_input} is {result}")