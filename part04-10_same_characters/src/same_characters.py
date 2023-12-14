# Write your solution here
def same_chars(word, char1, char2):
    # Ensure that char1 is less than or equal to char2
    char1, char2 = min(char1, char2), max(char1, char2)
    
    # Check if both indices are within the range of the string
    if 0 <= char1 < len(word) and 0 <= char2 < len(word):
        # Compare the characters at the specified indices
        return word[char1] == word[char2]
    else:
        # Return False if either index is out of range
        return False

# You can test your function by calling it within the following block
if __name__ == "__main__":
    print(same_chars("coder", 1, 2))
    print(same_chars("programmer", 6, 7))
