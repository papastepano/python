# Write your solution here
def most_common_character(input_string: str) -> str:
    char_count = {}
    most_common_char = input_string[0]

    for char in input_string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

        # Update most_common_char if the current character has more occurrences
        if char_count[char] > char_count[most_common_char]:
            most_common_char = char

    return most_common_char


