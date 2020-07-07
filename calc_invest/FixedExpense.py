# import pandas as pd
# import numpy as np
# from .Expense import Expense

# class FixedExpense(Expense):
    
#     def __init__(self, name, monthly_total):
#         Expense.__init__(self, total, has_interest=False)
        
#         """
#         Create objects with names to create tables of expenses broken down by monthly costs
        
#         Attributes:
#             name (str) name of the expense
#             total (float) cost per transaction of expense
#         """
#         self.name = name
#         self.total = total



#     def yearly_cost(self, has_interest):
#         # Might need to put into child classes rather than parent class
#         """
#         Calculates and returns the monthly cost of an expense
        
#         Args:
#             None
        
#         Returns:
#             float: approximate monthly cost
#         """

#         if has_interest == False:
#             yearly_cost = 1.0 * total * 12
#             return yearly_cost
#         else:

#     def apply_interest(self, interest_rate):
#     # write function to adjust costs that will integrate with fixed or interest expenses