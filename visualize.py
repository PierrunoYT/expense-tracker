import matplotlib.pyplot as plt
from expense_tracker import ExpenseTracker

def plot_expenses_by_category(tracker):
    """Create a pie chart of expenses by category"""
    totals = tracker.get_total_by_category()
    
    plt.figure(figsize=(10, 8))
    plt.pie(totals.values(), labels=totals.keys(), autopct='%1.1f%%')
    plt.title('Expenses by Category')
    plt.axis('equal')
    plt.show()

def plot_expenses_timeline(tracker):
    """Create a line plot of expenses over time"""
    expenses = tracker.get_expenses()
    dates = [exp['Date'] for exp in expenses]
    amounts = [float(exp['Amount']) for exp in expenses]
    
    plt.figure(figsize=(12, 6))
    plt.plot(dates, amounts, marker='o')
    plt.title('Expenses Over Time')
    plt.xlabel('Date')
    plt.ylabel('Amount')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
