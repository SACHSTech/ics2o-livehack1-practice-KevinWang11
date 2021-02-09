# asks the user to input the number of hours
hours = float(input("Enter the number of hours: "))

# calculates number of days & hours
days = int((hours // 24))
hours_remaining = int((hours % 24))

# prints the calculations above
print("Number of Days: "  + str(days))
print("Number of Hours: " + str(hours_remaining))