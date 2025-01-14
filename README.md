# Expense Tracker

A simple Python-based expense tracking tool that helps you log, categorize, and visualize your expenses.

## Features

- Log expenses with date, amount, category, and description
- Store expense data in CSV format
- Calculate totals by category
- Visualize expenses through:
  - Pie charts showing expense distribution by category
  - Timeline plots showing expenses over time

## Requirements

- Python 3.x
- matplotlib
- csv (built-in)
- datetime (built-in)

## Usage

```python
from expense_tracker import ExpenseTracker
from visualize import plot_expenses_by_category, plot_expenses_timeline

# Create a tracker instance
tracker = ExpenseTracker()

# Add some expenses
tracker.add_expense(50.00, "Groceries", "Weekly shopping")
tracker.add_expense(30.00, "Transportation", "Bus ticket")

# View expenses by category
print(tracker.get_total_by_category())

# Create visualizations
plot_expenses_by_category(tracker)
plot_expenses_timeline(tracker)
```

## File Structure

- `expense_tracker.py`: Main class for expense tracking functionality
- `visualize.py`: Visualization functions using matplotlib
- `expenses.csv`: Data storage file (created automatically)

## Data Storage

Expenses are stored in a CSV file with the following columns:
- Date (YYYY-MM-DD)
- Amount
- Category
- Description
