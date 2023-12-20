# Write your solution here
import string
def separate_characters(my_string: str):
    ascii_letters = []
    punctuation = []
    other = []

    for i in my_string:
        if i in string.ascii_letters:
            ascii_letters.append(i)
        elif i in string.punctuation:
            punctuation.append(i)
        else:
            other.append(i)
    return (''.join(ascii_letters), ''.join(punctuation), ''.join(other))

if __name__ == "__main__":
    parts = separate_characters("Olé!!! Hey, are ümläüts wörking?")
    print(parts[0])
    print(parts[1])
    print(parts[2])