# Write your solution here
import random
import string

def generate_strong_password(length: int,oneNumber=True, oneSpecial=True ):
    password = ""
    special_chars = "!?=+-()#"
    actualLenght = length
    if oneNumber: 
        actualLenght -= 1
        password += random.choice(string.digits)
    if oneSpecial:
        actualLenght -= 1
        password += random.choice(special_chars)

    for i in range(actualLenght):
        password += random.choice(string.ascii_letters).lower()

    random.shuffle(list(password))
    return password



if __name__ == "__main__":
    for i in range(10):
        print(generate_strong_password(8, True, True))
