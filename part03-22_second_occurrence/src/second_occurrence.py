# Write your solution here
string_input = input("Please type in a string: ")
substring_input = input("Please type in a substring: ")

first_occurrence = string_input.find(substring_input)
second_occurrence = string_input.find(substring_input, first_occurrence + len(substring_input))

if second_occurrence != -1:
    print(f"The second occurrence of the substring is at index {second_occurrence}.")
else:
    print("The substring does not occur twice in the string.")
