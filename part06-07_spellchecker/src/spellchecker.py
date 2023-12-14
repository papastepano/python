# write your solution here
user_input = input("Write text: ")

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