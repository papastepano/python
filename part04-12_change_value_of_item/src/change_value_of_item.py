# Write your solution here
predefined_list = [1, 2, 3, 4, 5]

while True:
    index = int(input("Index: "))
    
    # Check if the user entered -1 for the index
    if index == -1:
        break
    
    value = int(input("New value: "))
    
    # Replace the value at the given index
    predefined_list[index] = value
    
    # Print the updated list
    print(predefined_list)
