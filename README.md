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

## Installation & Setup

### Windows

```cmd
# Clone repository
git clone https://github.com/PierrunoYT/expense-tracker.git
cd expense-tracker

# Create and activate virtual environment
python -m venv venv
.\venv\Scripts\activate

# Install dependencies
pip install matplotlib
```

### macOS

```bash
# Clone repository
git clone https://github.com/PierrunoYT/expense-tracker.git
cd expense-tracker

# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip3 install matplotlib
```

### Linux

```bash
# Install Python if needed
sudo apt-get update
sudo apt-get install python3 python3-pip python3-venv

# Clone repository
git clone https://github.com/PierrunoYT/expense-tracker.git
cd expense-tracker

# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip3 install matplotlib
```

## Usage

### Running the Program

**Windows:**
```cmd
.\venv\Scripts\activate
python main.py
```

**macOS/Linux:**
```bash
source venv/bin/activate
python3 main.py
```

### Interactive Commands

Once running, the following commands are available:
```
add           - Add a new expense
list          - List all expenses
totals        - Show totals by category
viz pie       - Show pie chart of expenses
viz timeline  - Show timeline of expenses
help          - Show available commands
exit          - Exit the program
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

## Troubleshooting

### Windows
- If you get "python not found", ensure Python is added to your PATH
- Use `python` instead of `python3` for commands

### macOS
- Use `python3` instead of `python` for commands
- If matplotlib fails: `echo "backend: TkAgg" > ~/.matplotlib/matplotlibrc`

### Linux
- If matplotlib fails, install required system packages:
  ```bash
  sudo apt-get install python3-tk
  ```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'feat: add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.