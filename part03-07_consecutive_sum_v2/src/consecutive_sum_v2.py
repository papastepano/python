limit = int(input("Limit: "))
sum_of_numbers = 0
current_number = 1
verdict = ""

while sum_of_numbers < limit:
    sum_of_numbers += current_number
    verdict += f"{current_number} "
    if sum_of_numbers < limit:
        verdict += "+ "
    current_number += 1

verdict += "="
print("The consecutive sum: ", verdict, sum_of_numbers)