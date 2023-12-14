import math

# Write your solution here
def squared(text, size):
    index = 1
    string_length = len(text)
    repetitions_needed = (size * size) / string_length
    rounded_up = math.ceil(repetitions_needed)

    full_text = text * rounded_up

    while index <= size:
        print(full_text[:size])
        full_text = full_text[size:]
        index += 1

# Testing the function
if __name__ == "__main__":
    squared("ab", 3)
    print()
    squared("aybabtu", 5)