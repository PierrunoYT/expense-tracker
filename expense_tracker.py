"""
Expense Tracker Module

This module provides a simple expense tracking system that stores expenses in a CSV file.
It allows for adding expenses with dates, amounts, categories, and descriptions,
and provides methods for retrieving and analyzing expense data.

Example:
    >>> tracker = ExpenseTracker()
    >>> tracker.add_expense(20, "food", "lunch")
    >>> expenses = tracker.get_expenses()
    >>> totals = tracker.get_total_by_category()

The expenses are stored in a CSV file with the following format:
date;amount;category;description
14.01.2025;20;food;test
"""

from datetime import datetime
import csv
import os
from typing import Dict, List, Optional, Union

class ExpenseTracker:
    """A class to track and manage expenses using a CSV file for storage.

    The ExpenseTracker class provides methods to add expenses, retrieve all expenses,
    and calculate totals by category. It uses a CSV file for persistent storage,
    making the data easily portable and human-readable.

    Attributes:
        csv_file (str): Path to the CSV file used for storing expenses.
    """

    def __init__(self, csv_file: str = 'expenses.csv') -> None:
        """Initialize the ExpenseTracker with a specified CSV file.

        Args:
            csv_file: Path to the CSV file. Defaults to 'expenses.csv'.
        """
        self.csv_file = csv_file
        self._initialize_csv()
    
    def _initialize_csv(self) -> None:
        """Create CSV file with headers if it doesn't exist.

        This method checks if the specified CSV file exists and creates it
        with appropriate headers if it doesn't.
        """
        if not os.path.exists(self.csv_file):
            with open(self.csv_file, 'w', newline='') as file:
                writer = csv.writer(file, delimiter=';', quoting=csv.QUOTE_MINIMAL)
                writer.writerow(['date', 'amount', 'category', 'description'])
    
    def add_expense(self, amount: Union[int, float], category: str,
                   description: str = '', date: Optional[str] = None) -> None:
        """Add a new expense entry to the CSV file.

        Args:
            amount: The expense amount (integer or float)
            category: The expense category (e.g., 'food', 'transport')
            description: Optional description of the expense
            date: Optional date string in DD.MM.YYYY format. If not provided,
                  current date is used.

        Raises:
            ValueError: If the date string is not in DD.MM.YYYY format.
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
    
    def get_expenses(self) -> List[Dict[str, str]]:
        """Return all expenses as a list of dictionaries.

        Returns:
            A list of dictionaries, where each dictionary represents an expense
            with keys 'Date', 'Amount', 'Category', and 'Description'.
        """
        expenses = []
        with open(self.csv_file, 'r') as file:
            reader = csv.DictReader(file, delimiter=';', quoting=csv.QUOTE_MINIMAL)
            for row in reader:
                expenses.append(row)
        return expenses
    
    def get_total_by_category(self) -> Dict[str, float]:
        """Calculate total expenses by category.

        Returns:
            A dictionary mapping category names to their total amounts.
        """
        totals = {}
        expenses = self.get_expenses()
        for expense in expenses:
            category = expense['Category']
            amount = float(expense['Amount'])
            totals[category] = totals.get(category, 0) + amount
        return totals