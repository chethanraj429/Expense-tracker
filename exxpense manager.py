import json
import os
from datetime import datetime

current = datetime.now()
date = datetime.now().strftime("%d-%m-%Y")


def load_expenses():
    with open(r"D:/Python Files/my projects/Expense tracker/expenses.json", "r") as file:
        expenses = json.load(file)
    return expenses

def save_expenses(expenses):
    with open(r"D:/Python Files/my projects/Expense tracker/expenses.json", "w", encoding="utf-8") as file:

        json.dump(expenses, file, indent=4)

expenses=load_expenses()

def add_expense(expenses):
    categories = {
        "1":"Food",
        "2":"Transport",
        "3":"Shopping",
        "4":"Bills",
        "5":"Entertainment",
        "6":"Healthcare",
        "7":"Education",
        "8":"Other"
    }
    print("""
    Choose a category

        1. Food
        2. Transport
        3. Shopping
        4. Bills
        5. Entertainment
        6. Healthcare
        7. Education
        8. Other""")
    while True:
        category = input("Enter category (1-8): ")

        if category in categories:
            break

        print("Invalid category. Please choose 1-8.")
        
    description=input('enter the description:')
    
    while True:
        try:
            amount = float(input("Enter the expense: "))
            break
        except ValueError:
            print("Please enter a valid number.")
    expense={
        'date':date,
        'category':categories[category],
        'description':description,
        'amount':amount
        }
    expenses.append(expense)
    print("expense added successfully")
    return expenses
add_expense(expenses)


def view_expense(expenses):
    print(f"{'category':<20}{'description':<20}{'amount':<20}")
    total = 0
    for expense in expenses:
        print(f'{expense["category"]:<20}{expense["description"]:<20}{expense["amount"]:<20}')
        total += expense["amount"]
    print(f'{'TOTAL':<20}{'':<20}{total:<20}')



def update_expense(expenses):
    choice=input('add more expenses(yes/no):')
    while choice in ('yes','no'):
        if choice == 'yes':
            add_more_expense=add_expense(expenses)
            print(expenses)
            return(update_expense(expenses))
        if choice == 'no':
            save_expenses(expenses)
            return view_expense(expenses)
        else:
            print('invalid input please enter yes or no' )

def delete_expense(expenses):
    choice2=input('do you want to delete any expense(yes/no):')
    if choice2 == 'no':
        return
    view_expense(expenses)
    while True:
        try:
            expense_no=int(input("the expense log u want to delete:"))

            if 1<= expense_no <= len(expenses):
                expenses.pop(expense_no - 1)
                save_expenses(expenses)
                print('expense deleted successfully')
                break
            else:
                print('invalid expense no')

        except ValueError:
            print("please enter a valid number")


update_expense(expenses)






        
