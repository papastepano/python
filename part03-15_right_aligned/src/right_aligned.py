# Write your solution here
user_input = input("Please type in a string: ")
chars = 20
input_lenth = len(user_input)

stars = chars - input_lenth

print(stars*'*' + user_input)