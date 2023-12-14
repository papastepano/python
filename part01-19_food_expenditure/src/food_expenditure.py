# Get input from the user
times_per_week = int(input("How many times a week do you eat at the student cafeteria? "))
lunch_price = float(input("The price of a typical student lunch? "))
grocery_spending = float(input("How much money do you spend on groceries in a week? "))

# Calculate daily and weekly average food expenditure
daily_expenditure = (times_per_week * lunch_price + grocery_spending) / 7
weekly_expenditure = times_per_week * lunch_price + grocery_spending

# Print the results
print(f"\nAverage food expenditure:")
print(f"Daily: {daily_expenditure} euros")
print(f"Weekly: {weekly_expenditure} euros")
