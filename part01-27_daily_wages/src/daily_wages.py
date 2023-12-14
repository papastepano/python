# Get user input for hourly wage, hours worked, and day of the week
hourly_wage = float(input("Hourly wage: "))
hours_worked = float(input("Hours worked: "))
day_of_week = input("Day of the week: ")

# Calculate daily wages
if day_of_week.lower() == "sunday":
    daily_wages = hourly_wage * hours_worked * 2
else:
    daily_wages = hourly_wage * hours_worked

# Print the result
print(f"Daily wages: {daily_wages:.1f} euros")
