# Write your solution here
user_input = input("Word: ")
width = 30

word_len = len(user_input)
word_before = (width - 2 - word_len) // 2
word_after = width - 2 - word_before - word_len

print(width * "*")
print(f"*{word_before*' '}{user_input}{word_after*' '}*")
print(width * "*")