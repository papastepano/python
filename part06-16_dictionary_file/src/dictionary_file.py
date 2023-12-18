# Write your solution here
def add_word(fin, eng):
    with open("dictionary.txt", "a") as file:
        file.write(f"{fin} - {eng}\n")

while True:
    print("1 - Add word, 2 - Search, 3 - Quit")
    user_choice = int(input("Function: "))

    if user_choice == 3:
        print("Bye!")
        break
    elif user_choice == 2:
        search_term = input("Search term: ")
        with open("dictionary.txt", "r") as file:
            for line in file:
                line = line.replace("\n", "")
                if search_term in line:
                    print(line)

    elif user_choice == 1:
        finnish_word = input("The word in Finnish: ")
        english_word = input("The word in English: ")
        add_word(finnish_word, english_word)
        print("Dictionary entry added")