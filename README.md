# Expense Tracker

A simple and efficient Python-based expense tracking tool that helps you manage and analyze your expenses.

## Features

- Track expenses with date, amount, category, and description
- CSV-based storage for easy data portability
- Simple API for adding and retrieving expenses
- Calculate totals by category
- Flexible date handling (DD.MM.YYYY format)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/expense-tracker.git
cd expense-tracker
```

2. No additional dependencies required - uses Python standard library only!

## Usage

### Basic Usage

```python
from expense_tracker import ExpenseTracker

# Create a new tracker instance
tracker = ExpenseTracker()

# Add an expense
tracker.add_expense(
    amount=20,
    category="food",
    description="lunch",
    date="14.01.2025"  # Optional, defaults to current date
)

# Get all expenses
expenses = tracker.get_expenses()

# Get totals by category
totals = tracker.get_total_by_category()
```

### File Structure

The expenses are stored in a CSV file with the following format:
```
date;amount;category;description
14.01.2025;20;food;test
```

## Project Structure

- `expense_tracker.py`: Main implementation of the ExpenseTracker class
- `init_expenses.py`: Helper script to initialize the expenses file
- `expenses.csv`: Data storage file (auto-generated, git-ignored)

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'feat: add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.