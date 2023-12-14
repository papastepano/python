limit = int(input("Limit: "))
sum_of_numbers = 0
current_number = 1

while sum_of_numbers < limit:
    sum_of_numbers += current_number
    current_number += 1

print(sum_of_numbers)