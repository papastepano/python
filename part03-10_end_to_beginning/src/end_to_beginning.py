# Write your solution here
user_string = input("Please type in a string: ")
index = len(user_string) - 1

while 0 <= index < len(user_string):
    print(user_string[index])
    index -= 1