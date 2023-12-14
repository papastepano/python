# Taking input for the user's age
age = int(input("What is your age? "))

# Checking if the age is plausible
if 5 <= age <= 150:
    print("Ok, you're", age, "years old")
elif age < 0:
    print("That must be a mistake")
else:
    print("I suspect you can't write quite yet...")