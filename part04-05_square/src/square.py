# Copy here code of line function from previous exercise
def line(length, character):
    if len(character) == 0:
        character = '*'

    print(character[0] * length)

def square(size, character):
    charachters = size

    # You should call function line here with proper parameters
    while size != 0:
        line(charachters, character)
        size -= 1
    

# You can test your function by calling it within the following block
if __name__ == "__main__":
    square(5, "x")
    square(5, "+")