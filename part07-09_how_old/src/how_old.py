# Write your solution here
import datetime

day = int(input("Day: "))
month = int(input("Month: "))
year = int(input("Year: "))

new_millenium_eve = datetime.date(1999, 12, 31)
birthday = datetime.date(year, month, day)

age = new_millenium_eve - birthday

if age.days < 0:
    print("You weren't born yet on the eve of the new millennium.")
else:
    print(f"You were {age.days} days old on the eve of the new millennium.")
