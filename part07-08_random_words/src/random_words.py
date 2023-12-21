# Write your solution here
import random

def words(n: int, beginning: str):
    all_words = []
    selected_words = []

    with open("words.txt") as file:
        for line in file:
            line = line.replace("\n", "")
            if line.startswith(beginning):
                all_words.append(line)

    if len(all_words) < n:
        raise ValueError("Not enough words")
    
    while len(selected_words) < n:
        toAppend = random.choice(all_words)
        if toAppend not in selected_words:
            selected_words.append(toAppend)

    return selected_words

if __name__ == "__main__":
    print(words(3, "word"))