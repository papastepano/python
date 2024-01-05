# Write your solution here
def change_case(orig_string: str):
    new_string = ''
    for char in orig_string:
        if char.islower():
            new_string += char.upper()
        else:
            new_string += char.lower()
    return new_string

def split_in_half(orig_string: str):
    original_length = len(orig_string)
    half_length = original_length // 2
    first_half = orig_string[:half_length]
    second_half = orig_string[half_length:]
    return first_half, second_half
    pass

def remove_special_characters(orig_string: str):
    special_chars = "!§¤@#$%^&*()[]{};:,./<>?\|`~-=_+"
    for char in special_chars:
        orig_string = orig_string.replace(char, "")
    return orig_string

if __name__ == "__main__":
    import string_helper

    my_string = "Well hello there!"

    print(string_helper.change_case(my_string))

    p1, p2 = string_helper.split_in_half(my_string)

    print(p1)
    print(p2)

    m2 = string_helper.remove_special_characters("This is a test, lets see how it goes!!!11!")
    print(m2)