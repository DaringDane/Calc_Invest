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
            frequency (float) # of times per month this expense is payed
        """
    
    