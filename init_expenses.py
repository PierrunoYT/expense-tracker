#!/usr/bin/env python3
"""
Expense Tracker Initialization Script

This script demonstrates the usage of the ExpenseTracker class and can be used to
initialize a new expense tracking file with example data.

It can be run directly to create a new expenses.csv file with a sample expense:
    python init_expenses.py

The script serves both as an example of how to use the ExpenseTracker class
and as a utility to initialize a new expense tracking file.
"""

from expense_tracker import ExpenseTracker
from typing import Optional

def initialize_tracker(sample_data: bool = True) -> ExpenseTracker:
    """Initialize a new ExpenseTracker instance with optional sample data.

    Args:
        sample_data: Whether to add sample expense data. Defaults to True.

    Returns:
        An initialized ExpenseTracker instance.
    """
    # Create a new expense tracker instance
    tracker = ExpenseTracker()

    # Add a sample expense if requested
    if sample_data:
        tracker.add_expense(
            amount=20,
            category="food",
            description="test",
            date="14.01.2025"
        )

    return tracker

def main() -> None:
    """Main function to demonstrate ExpenseTracker usage."""
    print("Initializing Expense Tracker...")
    tracker = initialize_tracker()
    
    # Display the expenses
    expenses = tracker.get_expenses()
    print("\nCurrent expenses:")
    for expense in expenses:
        print(f"Date: {expense['date']}, "
              f"Amount: {expense['amount']}, "
              f"Category: {expense['category']}, "
              f"Description: {expense['description']}")
    
    # Display category totals
    totals = tracker.get_total_by_category()
    print("\nTotals by category:")
    for category, total in totals.items():
        print(f"{category}: {total}")

if __name__ == "__main__":
    main()