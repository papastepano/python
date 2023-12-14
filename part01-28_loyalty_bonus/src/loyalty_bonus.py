# Fix the program
initial_points = int(input("How many points are on your card? "))
if initial_points < 100:
    points = initial_points * 1.1
    print("Your bonus is 10 %")

if initial_points >= 100:
    points = initial_points * 1.15
    print("Your bonus is 15 %")

print("You now have", points, "points")