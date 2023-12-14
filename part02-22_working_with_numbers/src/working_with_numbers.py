print("Please type in integer numbers. Type in 0 to finish.")
numbers = []
positive_count = 0
negative_count = 0
while True:
    number = int(input("Number: "))

    if number > 0:
        positive_count += 1
    elif number < 0:
        negative_count += 1
    else:
        break
    numbers.append(number)
    print(f"... the program asks for numbers \nNumbers typed in {len(numbers)} \nThe sum of the numbers is {sum(numbers)} \nThe mean of the numbers is {sum(numbers)/len(numbers)} \nPositive numbers {positive_count} \nNegative numbers {negative_count}")
