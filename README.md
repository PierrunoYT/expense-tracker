# Expense Tracker

A simple Python-based expense tracking tool that helps you log, categorize, and visualize your expenses.

## Installation

### Prerequisites
- Python 3.x installed on your system
- pip (Python package installer)

### Windows
```bash
# Clone the repository
git clone https://github.com/yourusername/expense-tracker.git
cd expense-tracker

# Create and activate virtual environment
python -m venv venv
.\venv\Scripts\activate

# Install requirements
pip install matplotlib
```

### macOS/Linux
```bash
# Clone the repository
git clone https://github.com/yourusername/expense-tracker.git
cd expense-tracker

# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate

# Install requirements
pip install matplotlib
```

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

### Running the Program

#### Windows
```bash
# Activate virtual environment (if not already activated)
.\venv\Scripts\activate

# Run Python in interactive mode
python
```

#### macOS/Linux
```bash
# Activate virtual environment (if not already activated)
source venv/bin/activate

# Run Python in interactive mode
python3
```

### CLI Commands

```bash
# Add an expense
python main.py add 50.00 Groceries -d "Weekly shopping"

# List all expenses
python main.py list

# Show totals by category
python main.py totals

# Visualize expenses (pie chart)
python main.py viz pie

# Visualize expenses (timeline)
python main.py viz timeline

# Show help
python main.py --help
```

### Notes
- The expenses.csv file will be created automatically in your working directory
- Make sure your virtual environment is activated before running the code
- To exit Python interactive mode, type `exit()` or press Ctrl+Z (Windows) / Ctrl+D (macOS/Linux)

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
