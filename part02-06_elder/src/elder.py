# Person 1
name1 = input("Person 1:\nName: ")
age1 = int(input("Age: "))

# Person 2
name2 = input("Person 2:\nName: ")
age2 = int(input("Age: "))

# Comparing ages
if age1 > age2:
    print("The elder is", name1)
elif age1 < age2:
    print("The elder is", name2)
else:
    print(name1, "and", name2, "are the same age")
