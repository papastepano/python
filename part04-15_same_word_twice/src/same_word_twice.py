# Write your solution here
my_list = []

while True:
    word = input("Word: ")
    if word not in my_list:
        my_list.append(word)
    else:
        break

print(f"You typed in {len(my_list)} different words")