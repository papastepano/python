# Write your solution here
import random
import string

def generate_password(length: int):
    password = ""
    for i in range(length):
        password += random.choice(string.ascii_letters).lower()
    return password



if __name__ == "__main__":
    for i in range(10):
        print(generate_password(8))
