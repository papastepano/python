# Get user input for tomorrow's weather forecast
print("What is the weather forecast for tomorrow?")
temperature = int(input("Temperature: "))
rain_forecast = input("Will it rain (yes/no): ").lower()
# Initial clothing suggestion
clothing_suggestion = "Wear jeans and a T-shirt"

# Adjust clothing suggestion based on temperature
if temperature > 20:
    pass  # No change to initial suggestion
elif temperature > 10:
    clothing_suggestion += "\nI recommend a jumper as well"
elif temperature > 5:
    clothing_suggestion += "\nI recommend a jumper as well\nTake a jacket with you"
else:
    clothing_suggestion += "\nI recommend a jumper as well\nTake a jacket with you\nMake it a warm coat, actually\nI think gloves are in order"

# Adjust clothing suggestion based on rain forecast
if rain_forecast == "yes":
    clothing_suggestion += "\nDon't forget your umbrella!"

# Print the final clothing suggestion
print(clothing_suggestion)