import json
import os
from datetime import datetime

EXPENSES_FILE = 'expenses.json'

def load_expenses():
    """Load expenses from a JSON file."""
    if os.path.exists(EXPENSES_FILE):
        with open(EXPENSES_FILE, 'r') as file:
            return json.load(file)
    return []

def save_expenses(expenses):
    """Save expenses to a JSON file."""
    with open(EXPENSES_FILE, 'w') as file:
        json.dump(expenses, file, indent=4)

def add_expense(description, amount):
    """Add a new expense."""
    expenses = load_expenses()
    expense = {
        'description': description,
        'amount': amount,
        'date': datetime.now().strftime('%d-%m-%y %H:%M:%S')
    }
    expenses.append(expense)
    save_expenses(expenses)
    print(f"Added expense: '{description}' - ${amount:.2f}")

def view_expenses():
    """View all recorded expenses."""
    expenses = load_expenses()
    if not expenses:
        print("No expenses recorded.")
        return
    print("\nExpenses:")
    total_amount = 0
    for index, expense in enumerate(expenses):
        print(f"{index + 1}. [{expense['date']}] {expense['description']} - Rs. {expense['amount']:.2f}")
        total_amount += expense['amount']
    print(f"Total expenses: Rs. {total_amount:.2f}")

def delete_expense(index):
    """Delete an expense by index."""
    expenses = load_expenses()
    if index < 1 or index > len(expenses):
        print("Invalid index.")
        return
    removed = expenses.pop(index - 1)
    save_expenses(expenses)
    print(f"Deleted expense: '{removed['description']}' - ${removed['amount']:.2f}")

def main():
    """Main loop of the application."""
    while True:
        print("\n--- Expense Tracker ---")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Delete Expense")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            description = input("Enter expense description: ")
            amount = float(input("Enter expense amount: "))
            add_expense(description, amount)
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            view_expenses()
            try:
                index = int(input("Enter the expense number to delete: "))
                delete_expense(index)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == '4':
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()