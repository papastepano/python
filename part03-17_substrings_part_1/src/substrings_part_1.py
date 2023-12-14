# Write your solution here
user_input = input("Please type in a string: ")
length = len(user_input)

index = 0

while index<=length:
    print(user_input[0:index])
    index += 1;