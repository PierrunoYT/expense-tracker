from expense_tracker import ExpenseTracker

# Create a new expense tracker instance
# This will automatically create the CSV file with the new structure
tracker = ExpenseTracker()

# Add a test expense with the exact format from the image
tracker.add_expense(20, "food", "test", "14.01.2025")