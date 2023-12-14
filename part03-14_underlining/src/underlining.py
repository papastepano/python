# Write your solution here
while True:
    user_input = input("Please type in a string: ")
    
    if not user_input:
        break  # Exit the loop if an empty string is entered
    
    print(user_input)
    print('-' * len(user_input))
