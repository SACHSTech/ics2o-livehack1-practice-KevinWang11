# asks the user for the number of minutes
minutes = float(input("Enter the number of minutes: "))

# calculates the number of days, hours and minutes according to user input
days = int((minutes // 1440))
hours = int(((minutes % 1440) // 60))
minutes_2 = int(((minutes % 1440) % 60))

# prints out the answer for the user
print("Number of Days: "  + str(days))
print("Number of Hours: "  + str(hours))
print("Number of Minutes: "  + str(minutes_2))