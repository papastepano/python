# Write your solution here
user_input = int(input("Please type in a number: "))
operand1 = 1
operand2 = 1

while operand1 <= user_input:
    while operand2 <= user_input:
        print(f"{operand1} x {operand2} = {operand1 * operand2}")
        operand2 += 1
    operand1 += 1
    operand2 = 1