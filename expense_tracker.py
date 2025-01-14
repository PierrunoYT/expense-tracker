from datetime import datetime
import csv
import os

class ExpenseTracker:
    def __init__(self, csv_file='expenses.csv'):
        self.csv_file = csv_file
        self._initialize_csv()
    
    def _initialize_csv(self):
        """Create CSV file with headers if it doesn't exist"""
        if not os.path.exists(self.csv_file):
            with open(self.csv_file, 'w', newline='') as file:
                writer = csv.writer(file, delimiter=';', quoting=csv.QUOTE_MINIMAL)
                writer.writerow(['date', 'amount', 'category', 'description'])
    
    def add_expense(self, amount, category, description='', date=None):
        """Add a new expense entry
        
        Args:
            amount: The expense amount
            category: The expense category
            description: Optional description of the expense
            date: Optional date string in DD.MM.YYYY format. If not provided, current date is used.
        """
        if date is None:
            date = datetime.now().strftime('%d.%m.%Y')
        else:
            # Validate date format
            try:
                datetime.strptime(date, '%d.%m.%Y')
            except ValueError:
                raise ValueError("Date must be in DD.MM.YYYY format")
        with open(self.csv_file, 'a', newline='') as file:
            writer = csv.writer(file, delimiter=';', quoting=csv.QUOTE_MINIMAL)
            writer.writerow([date, amount, category, description])
    
    def get_expenses(self):
        """Return all expenses as a list of dictionaries"""
        expenses = []
        with open(self.csv_file, 'r') as file:
            reader = csv.DictReader(file, delimiter=';', quoting=csv.QUOTE_MINIMAL)
            for row in reader:
                expenses.append(row)
        return expenses
    
    def get_total_by_category(self):
        """Calculate total expenses by category"""
        totals = {}
        expenses = self.get_expenses()
        for expense in expenses:
            category = expense['Category']
            amount = float(expense['Amount'])
            totals[category] = totals.get(category, 0) + amount
        return totals
