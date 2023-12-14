# Write your solution here

original_list = []

while True:
    item = int(input("New item: "))
    if item == 0:
        break
    else:
        original_list.append(item)
        print(f"The list now: {str(original_list)}")
        print(f"The list in order: {str(sorted(original_list))}")

print("Bye!")