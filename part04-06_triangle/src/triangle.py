# Copy here code of line function from previous exercise
def line(length, character):
    if len(character) == 0:
        character = '*'

    print(character[0] * length)

def triangle(size):
    current_print = 1
    # You should call function line here with proper parameters
    while current_print <= size:
        line(current_print, "#")
        current_print += 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    triangle(6)
    print()
    triangle(3)
    print()
    triangle(5)
