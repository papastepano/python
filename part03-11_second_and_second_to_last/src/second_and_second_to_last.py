# Write your solution here
user_input = input("Please type in a string: ")

second = user_input[1]
second_last = user_input[-2]

if second == second_last:
    print("The second and the second to last characters are", second)
else:
    print("The second and the second to last characters are different")

