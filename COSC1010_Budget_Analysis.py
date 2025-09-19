#
# Victor Byrd
# 9-18-2025
# Budget Analysis Programming Project
# COSC 1010
#
# Use comments liberally throughout the program. 

def main():
    # Ask the user for the budgeted amount for the month
    budget = float(input("Enter the amount you have budgeted for the month: $"))
    
    # This variable will keep track of the running total of expenses
    total_expenses = 0.0
    
    print("Enter your expenses one by one.")
    print("Type 'done' when you are finished.\n")
    
    # Start a loop that will keep asking for expenses until the user types 'done'
    while True:
        # Prompt user for an expense
        expense = input("Enter an expense (or 'done' to finish): ")
        
        # If the user is done entering expenses, break out of the loop
        if expense.lower() == "done":
            break
        
        try:
            # Convert the expense to a number and add it to the running total
            total_expenses += float(expense)
        except ValueError:
            # If the user types something invalid, show an error message
            print("Please enter a valid number or 'done'.")
    
    # After the loop finishes, display the budget summary
    print("\nBudget Summary:")
    print(f"Budgeted: ${budget:.2f}")      # Show the original budget
    print(f"Expenses: ${total_expenses:.2f}")  # Show total expenses entered
    
    # Calculate the difference between budget and expenses
    difference = budget - total_expenses
    
    # Display if the user is under, over, or exactly on budget
    if difference > 0:
        print(f"You are UNDER budget by ${difference:.2f}")
    elif difference < 0:
        print(f"You are OVER budget by ${abs(difference):.2f}")
    else:
        print("You are exactly ON budget!")

# Run the program
main()
