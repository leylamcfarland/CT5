# Part 1: Average Rainfall Calculation

# Ask the user for the number of years
num_years = int(input("Enter the number of years: "))

# Initialize total rainfall and total months
total_rainfall = 0
total_months = num_years * 12

# Outer loop to iterate over each year
for year in range(1, num_years + 1):
    print(f"\nYear {year}")
    # Inner loop to iterate over each month
    for month in range(1, 13):
        while True:  # Validate input to ensure it's a positive number
            try:
                rainfall = float(input(f"Enter the inches of rainfall for month {month}: "))
                if rainfall < 0:
                    print("Please enter a non-negative value.")
                else:
                    break
            except ValueError:
                print("Invalid input. Please enter a number.")
        total_rainfall += rainfall

# Calculate the average rainfall
average_rainfall = total_rainfall / total_months

# Display the results
print("\nTotal number of months:", total_months)
print("Total inches of rainfall:", total_rainfall)
print(f"Average rainfall per month: {average_rainfall:.2f} inches")