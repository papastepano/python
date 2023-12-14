# Write your solution here
user_input = int(input("Please type in a number: "))
number = 1
even_arr = []
odd_arr = []

while number <= user_input:
    if number % 2 == 0:
        even_arr.append(number)
    else: 
        odd_arr.append(number)

    number += 1

# Combine and print the flipped pairs
result_arr = []
i = 0
while i < len(even_arr):
    result_arr.append(even_arr[i])
    result_arr.append(odd_arr[i])
    i += 1

for index in result_arr:
    print(index)

if user_input % 2 != 0:
    print(user_input)
