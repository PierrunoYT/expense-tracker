from expense_tracker import ExpenseTracker
from visualize import plot_expenses_by_category, plot_expenses_timeline

def print_help():
    """Print available commands"""
    print("\nAvailable commands:")
    print("  add     - Add a new expense")
    print("  list    - List all expenses")
    print("  totals  - Show totals by category")
    print("  viz pie - Show pie chart of expenses")
    print("  viz timeline - Show timeline of expenses")
    print("  help    - Show this help message")
    print("  exit    - Exit the program")

def main():
    print("Welcome to Expense Tracker!")
    print("Type 'help' for available commands")
    
    tracker = ExpenseTracker()
    
    while True:
        try:
            command = input("\n> ").strip().lower()
            
            if command == "exit":
                print("Goodbye!")
                break
                
            elif command == "help":
                print_help()
                
            elif command == "add":
                try:
                    amount = float(input("Amount: "))
                    category = input("Category: ")
                    description = input("Description (optional): ")
                    
                    tracker.add_expense(amount, category, description)
                    print(f"Added expense: {amount} in {category}")
                except ValueError:
                    print("Error: Amount must be a number")
                
            elif command == "list":
                expenses = tracker.get_expenses()
                if not expenses:
                    print("No expenses recorded yet")
                for expense in expenses:
                    print(f"{expense['Date']}: {expense['Amount']} ({expense['Category']}) - {expense['Description']}")
                
            elif command == "totals":
                totals = tracker.get_total_by_category()
                if not totals:
                    print("No expenses recorded yet")
                for category, total in totals.items():
                    print(f"{category}: {total:.2f}")
                
            elif command == "viz pie":
                plot_expenses_by_category(tracker)
                
            elif command == "viz timeline":
                plot_expenses_timeline(tracker)
                
            else:
                print("Unknown command. Type 'help' for available commands")
                
        except KeyboardInterrupt:
            print("\nUse 'exit' to quit")
        except Exception as e:
            print(f"Error: {str(e)}")

if __name__ == '__main__':
    main()
