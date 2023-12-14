# Taking input for a year
year = int(input("Please type in a year: "))

# Checking leap year conditions
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("That year is a leap year.")
else:
    print("That year is not a leap year.")
