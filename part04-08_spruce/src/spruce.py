# Write your solution here
def spruce(size):
    print("a spruce!")

    i = 1
    while i <= size:
        spaces = " " * (size - i)
        stars = "*" * (2 * i - 1)
        print(spaces + stars)
        i += 1

    # Print the trunk
    trunk_space = " " * (size - 1)
    print(trunk_space + "*")
    
# You can test your function by calling it within the following block
if __name__ == "__main__":
    spruce(5)