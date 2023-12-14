# Taking input for the first word
word1 = input("Please type in the 1st word: ")

# Taking input for the second word
word2 = input("Please type in the 2nd word: ")

# Comparing the words
if word1 < word2:
    print(word2, "comes alphabetically last.")
elif word1 > word2:
    print(word1, "comes alphabetically last.")
else:
    print("You gave the same word twice.")
