# Get user input for temperature in degrees Fahrenheit
temperature_f = float(input("Please type in a temperature (F): "))

# Convert Fahrenheit to Celsius using the formula: (F - 32) * 5/9
temperature_c = (temperature_f - 32) * 5/9

# Print the converted temperature in degrees Celsius
print(f"{temperature_f} degrees Fahrenheit equals {temperature_c} degrees Celsius")

# Check if the temperature is below zero degrees Celsius and print a message if true
if temperature_c < 0:
    print("Brr! It's cold in here!")
