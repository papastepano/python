# Write your solution here
def longest(strings: list) -> str:
    string_lengths = []

    for s in strings:
        string_lengths.append(len(s))

    return strings[string_lengths.index(max(string_lengths))]

if __name__ == "__main__":
    strings = ["hi", "hiya", "hello", "howdydoody", "hi there"]
    print(longest(strings))