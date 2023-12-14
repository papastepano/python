# Write your solution here
my_list = []

print("The list is now " + str(my_list))

while True:
    choice = input("a(d)d, (r)emove or e(x)it: ")
    if choice == "d":
        my_list.append(len(my_list) + 1)
        print("The list is now " + str(my_list))
    elif choice == "r":
        my_list.pop()
        print("The list is now " + str(my_list))
    elif (choice == "x"):
        break

print("Bye!")