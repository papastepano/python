# write your solution here
import difflib 
user_input = input("Write text: ")
suggestions = {}

with open("wordlist.txt") as wordlist:
    word_list = []
    for word in wordlist:
        word = word.replace("\n", "")
        word_list.append(word.lower())

misspelled_words = []
input_array = user_input.split(" ")

for i in input_array:
    if i.lower() not in word_list:
        misspelled_words.append(i)

for res in input_array:
    if res not in misspelled_words:
        print(f"{res} ", end="")
    else:
        print(f"*{res}* ", end="")
        suggestions[res] = difflib.get_close_matches(res, word_list)

print("\nsuggestions:")
for key, value in suggestions.items():
    print(f"\n{key}: ", end="")
    print(", ".join(value))