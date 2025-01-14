from expense_tracker import ExpenseTracker

# Create a new expense tracker instance
# This will automatically create the CSV file with the new structure
tracker = ExpenseTracker()

# Add a test expense
tracker.add_expense(20.0, "food", "test")