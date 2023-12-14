# Write your solution here
def no_shouting(input_strings: []):
    result = []
    for word in input_strings:
        if not word.isupper():
            result.append(word)

    return result