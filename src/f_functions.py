# Franco's Budget and Expenses function's
from helper import *

def view_entries(user):
    print("What kind of entry would you like to view?\n")
    print("1. Income\n2. Expenses\n3. Savings\n4. All Entries")

    choice = inputchecker(4)

    if choice == 1:
        incomes = user.income.keys()
        for income in incomes:
            print(incomes[income])
    elif choice == 2:
        expenses = user.expense.keys()
        for expense in expenses:
            print(expenses[expense])
    elif choice == 3:
        savings = user.saving.keys()
        for saving in savings:
            print(savings[saving])
    elif choice == 4:
        entries = user.income.keys() + user.expense.keys() + user.saving.keys()
        for entry in entries:
            print(entries[entry])
    else:
        print("Invalid choice. Please try again.")
