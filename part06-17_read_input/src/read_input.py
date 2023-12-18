# Write your solution here
def read_input(msg: str, min: int, max: int):
    while True:
        try:
            user_input = int(input(msg))
            if user_input < min or user_input > max:
                raise ValueError
            return user_input
        except ValueError:
            print(f"You must type in an integer between {min} and {max}")

if __name__ == "__main__":
    number = read_input("Please type in a number: ", 5, 10)
    print("You typed in:", number)