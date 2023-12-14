word = input("Please type in a word: ")
start_char = input("Please type in a character: ")

while len(word) >= 3:
    if word[0] == start_char:
        print(word[:3])
    word = word[1:]