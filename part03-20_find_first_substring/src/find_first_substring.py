# Write your solution here
user_word = input("Please type in a word: ")
user_character = input("Please type in a character: ")

check = user_word.find(user_character)

if(check >= 0):
    to_print = user_word[check:check+3]
    if len(to_print) == 3:
        print(to_print)