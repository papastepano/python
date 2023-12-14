# Write your solution here
user_input = int(input("Please type in a number: "))
number = 1
arr = []

while number <= user_input:
    arr.append(number)
    number += 1

if user_input % 2 == 0:
    while len(arr) > 0: 
        print(arr[0])
        print(arr[-1])
        del arr[0]
        del arr[-1]
else:
    while len(arr) > 1: 
        print(arr[0])
        print(arr[-1])
        del arr[0]
        del arr[-1]
    if len(arr) == 1:
        print(arr[0])
        del arr[0]
