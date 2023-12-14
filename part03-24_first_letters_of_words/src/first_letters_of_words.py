# Write your solution here
sentence = input("Please type in a sentence: ")
word_count = len(sentence.split())
words = sentence.split()
iteration = 0

while iteration < word_count:
    print(words[iteration][0])
    iteration += 1