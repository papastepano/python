# Write your solution here
password = input("Password: ")

while True:
    repeat = input("Repeat password: ")

    if password == repeat:
        print("User account created!")
        break
    
    print("They do not match!")
