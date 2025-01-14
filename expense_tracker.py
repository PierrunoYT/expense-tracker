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
                writer = csv.writer(file, delimiter=',', quoting=csv.QUOTE_MINIMAL)
                writer.writerow(['Date', 'Amount', 'Category', 'Description'])
    
    def add_expense(self, amount, category, description=''):
        """Add a new expense entry"""
        date = datetime.now().strftime('%Y-%m-%d')
        with open(self.csv_file, 'a', newline='') as file:
            writer = csv.writer(file, delimiter=',', quoting=csv.QUOTE_MINIMAL)
            writer.writerow([date, amount, category, description])
    
    def get_expenses(self):
        """Return all expenses as a list of dictionaries"""
        expenses = []
        with open(self.csv_file, 'r') as file:
            reader = csv.DictReader(file, delimiter=',', quoting=csv.QUOTE_MINIMAL)
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
