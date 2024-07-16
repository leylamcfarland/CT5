# Book Club Points Calculation Program

# Ask the user for the number of books purchased
num_books = int(input("Enter the number of books purchased this month: "))

# Determine the points based on the number of books
if num_books == 0:
    points = 0
elif num_books == 2:
    points = 5
elif num_books == 3:
    points = 5
elif num_books == 4:
    points = 15
elif num_books == 5:
    points = 15
elif num_books == 6:
    points = 30
elif num_books == 7:
    points = 30
elif num_books >= 8:
    points = 60
else:
    points = 0  # Handle cases where number of books does not match any specific condition

# Display the points awarded
print(f"Points awarded: {points}")