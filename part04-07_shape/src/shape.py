# Copy here code of line function from previous exercise and use it in your solution
def line(length, character):
    if len(character) == 0:
        character = '*'

    print(character[0] * length)

def triangle(size, character):
    current_print = 1
    # You should call function line here with proper parameters
    while current_print <= size:
        line(current_print, character)
        current_print += 1

def square_of_hashes(width, height, filler):
    while height != 0:
        line(width, filler)
        height -= 1
    
def shape(width, character, height, filler):
    triangle(width, character)
    square_of_hashes(width, height, filler)

# You can test your function by calling it within the following block
if __name__ == "__main__":
    shape(5, "x", 2, "o")