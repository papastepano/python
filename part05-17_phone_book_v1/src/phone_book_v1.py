# Write your solution here
book = {}

while True:
    command = int(input("command (1 search, 2 add, 3 quit): "))

    if command == 1:
        name = input("name: ")
        if name in book:
            print(book[name])
        else:
            print("no number")
    
    elif command == 2:
        name = input("name: ")
        number = input("number: ")
        
        book[name] = number

        print("ok!")

    elif command == 3:
        print("quitting...")
        break

    else:
        print("Something went wrong!")