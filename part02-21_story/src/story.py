words = []
while True:
    word = input("Please type in a word: ")
    if (word.lower() == "end") or (words and len(word) and word.lower() == words[-1]):
        break
    words.append(word)

story = " ".join(words)
print(story)
