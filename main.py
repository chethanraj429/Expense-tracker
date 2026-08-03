from expense_manager import (
     add_expense,
    view_expense,
    update_expense,
    delete_expense,
    search_by_category
)
from file_handler import load_expenses

print("Program started")
expenses = load_expenses()

print("Expenses loaded")

while True:
    print("""
1. Add Expense
2. View Expense
3. Update Expense
4. Delete Expense
5. Exit
""")

    choose = input("Choice: ")

    if choose == "1":
        add_expense(expenses)

    elif choose == "2":
        view_expense(expenses)

    elif choose == "3":
        update_expense(expenses)

    elif choose == "4":
        delete_expense(expenses)

    elif choose == "5":
        search_by_category(expenses)
    else:
        print('Invalid choice')
