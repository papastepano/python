# Get user input for the name
name = input("Please enter your name: ")

# Check if the name is "Jerry"
if name == "Jerry":
    print("Hello Jerry! Your meal is on the house.")
else:
    # If the name is not "Jerry," ask for the number of portions
    portions = int(input("Please enter the number of portions: "))
    
    # Calculate the total cost for the given number of portions
    price_per_portion = 5.90
    total_cost = portions * price_per_portion
    
    # Print the total cost
    print(f"The total cost is {total_cost}")
print("Next please!")
