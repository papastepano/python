# Write your solution here
def no_vowels(input_string: str) -> str:
    vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
    result = ""
    for char in input_string:
        if char not in vowels:
            result += char
    return result