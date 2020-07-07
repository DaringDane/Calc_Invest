import pandas as pd
import numpy as np
# from .Expense import Expense

def build_expense_table():

    """
    Constructs a table of expensess

    Args:
        None
    
    Returns:
        Dataframe with expense data
    """

    expenses = {'name':[], 'monthly_total':[]}

    new_entry = True
    while new_entry is True:
        expense = input("Please enter an expense name, and total spent on it per month on average, separated by a comma and space: ").split(', ')
        ### NEED regex to ensure comma format
        if expense[0] in expenses.keys():
            print("That expense has already been entered.")
        else:    
            expenses['name'].append(expense[0])
            expenses['monthly_total'].append(float(expense[1]))
        i = 0
        while i < 1:
            another = input("Add another expense? (answer Y or N): ").lower()
            if another == 'n':
                new_entry = False
                i += 1
            elif another == 'y':
                i += 1
            else:
                print("Invalid entry - please type either Y or N")

    return pd.DataFrame(expenses)

    if __name__ == '__main__':
        main()
