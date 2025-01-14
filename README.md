# Expense Tracker

A simple Python-based expense tracking tool that helps you log, categorize, and visualize your expenses through an interactive CLI interface.

## Features

- Interactive command-line interface
- Track expenses with date, amount, category, and description
- CSV-based storage for easy data portability
- Calculate totals by category
- Visualize expenses through:
  - Pie charts showing expense distribution by category
  - Timeline plots showing expenses over time

## Requirements

- Python 3.x
- matplotlib (for visualizations)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/PierrunoYT/expense-tracker.git
cd expense-tracker
```

2. Install required packages:
```bash
pip install matplotlib
```

## Usage

### Interactive CLI

Run the program:
```bash
python main.py
```

### Data Storage

The expenses are stored in a CSV file with the following format:
```
date;amount;category;description
14.01.2025;20;food;test
```

### Programmatic Usage

```python
from expense_tracker import ExpenseTracker
from visualize import plot_expenses_by_category, plot_expenses_timeline

# Create a tracker instance
tracker = ExpenseTracker()

# Add an expense
tracker.add_expense(
    amount=50.00,
    category="Groceries",
    description="Weekly shopping",
    date="14.01.2025"  # Optional, defaults to current date
)

# Get all expenses
expenses = tracker.get_expenses()

# Get totals by category
totals = tracker.get_total_by_category()

# Create visualizations
plot_expenses_by_category(tracker)
plot_expenses_timeline(tracker)
```

## Project Structure

- `main.py`: Interactive CLI interface
- `expense_tracker.py`: Core expense tracking functionality
- `visualize.py`: Visualization functions using matplotlib
- `init_expenses.py`: Helper script to initialize expenses file
- `expenses.csv`: Data storage file (auto-generated, git-ignored)

## Files Description

- `expense_tracker.py`: Contains the ExpenseTracker class with methods for adding and retrieving expenses
- `visualize.py`: Provides visualization functions using matplotlib for creating pie charts and timeline plots
- `main.py`: Implements the interactive command-line interface
- `init_expenses.py`: Helper script for initializing the expense tracking system

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'feat: add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.