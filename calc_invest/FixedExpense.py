import pandas as pd
import numpy as np
from .Expense import Expense

class FixedExpense(Expense):
    
    def __init__(self, name, total, frequency):
        Expense.__init__(self, total, frequency)
        
        """
        Create objects with names to create tables of expenses broken down by monthly costs
        
        Attributes:
            name (str) name of the expense
            total (float) cost per transaction of expense
        """
        self.name = name
        self.total = total

    def build_expense_table(self):

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
            expense = input("Please enter an expense name, and total spent on it per month \
                             on average, separated by a comma and space: ").split(', ')
            ### NEED regex to ensure comma format
            expenses['name'].append(expense[0])
            expenses['monthly_total'].append(expense[1])
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

        expenses = pd.DataFrame(expenses)

        return expenses