import json

def load_expenses():
    with open(r"D:/Python Files/my projects/Expense tracker/expenses.json", "r") as file:
        expenses = json.load(file)
    return expenses

def save_expenses(expenses):
    with open(r"D:/Python Files/my projects/Expense tracker/expenses.json", "w", encoding="utf-8") as file:

        json.dump(expenses, file, indent=4)