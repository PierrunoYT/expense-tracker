import argparse
from expense_tracker import ExpenseTracker
from visualize import plot_expenses_by_category, plot_expenses_timeline

def main():
    parser = argparse.ArgumentParser(description='Expense Tracker CLI')
    subparsers = parser.add_subparsers(dest='command', help='Commands')

    # Add expense command
    add_parser = subparsers.add_parser('add', help='Add a new expense')
    add_parser.add_argument('amount', type=float, help='Expense amount')
    add_parser.add_argument('category', help='Expense category')
    add_parser.add_argument('-d', '--description', help='Expense description', default='')

    # List expenses command
    subparsers.add_parser('list', help='List all expenses')

    # Show totals command
    subparsers.add_parser('totals', help='Show totals by category')

    # Visualize commands
    viz_parser = subparsers.add_parser('viz', help='Visualize expenses')
    viz_parser.add_argument('type', choices=['pie', 'timeline'], help='Type of visualization')

    args = parser.parse_args()
    tracker = ExpenseTracker()

    if args.command == 'add':
        tracker.add_expense(args.amount, args.category, args.description)
        print(f"Added expense: {args.amount} in {args.category}")
    
    elif args.command == 'list':
        expenses = tracker.get_expenses()
        for expense in expenses:
            print(f"{expense['Date']}: {expense['Amount']} ({expense['Category']}) - {expense['Description']}")
    
    elif args.command == 'totals':
        totals = tracker.get_total_by_category()
        for category, total in totals.items():
            print(f"{category}: {total:.2f}")
    
    elif args.command == 'viz':
        if args.type == 'pie':
            plot_expenses_by_category(tracker)
        else:
            plot_expenses_timeline(tracker)
    
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
