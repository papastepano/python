# Write your solution here
import math
user_input = int(input("Width: "))
user_input_height = int(input("Height: "))
character = "#"
current_line = 0

while 0 <= current_line < user_input_height:
    print(character*user_input)
    current_line += 1

