# asks the user to input the temperature and the wind speed
temp = float(input("Enter the temperature here: "))
wind = float(input("Enter the wind speed here in km/h: "))

# calculates windchill 
windchill = ((35.74 + 0.6215 * (temp)) - (35.75 * (wind) ** 0.16) + (0.4275 * (temp)) * ((wind) ** 0.16))

# outputs the windchill factor to the user
print("This is the windchill factor: " + str(round(windchill, 2)))

