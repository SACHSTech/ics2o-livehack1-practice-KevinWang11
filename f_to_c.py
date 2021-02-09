# asks the user for the temperature in farenheit
farenheit = float(input("Enter temperature in farenheit: "))

# calculates the temperature in celsius using the formula
celsius = str(round((farenheit - 32) * (5/9)))

# prints the temperature in celsius to the user's screen
print("This is the temperature in Celsius: " + celsius)