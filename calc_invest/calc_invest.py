import pandas as pd
import numpy as np

from build_tables import build_expense_table
from Investment import Investment_Snapshot


finance_base = input("Enter annual taxable income, current investment totals, expected pct dividends from investments(decimal), and tax filing status(single = single, mfj = married, filing jointly, mfs = married, filing separately, hoh = head of households): ").split(', ')

annual_taxable_income, current_investments, expected_pct_dividends, filing_status = \
    float(finance_base[0]), float(finance_base[1]), float(finance_base[2]), str(finance_base[3])

finances = Investment_Snapshot(annual_taxable_income, current_investments, expected_pct_dividends, filing_status)

# net_takehome = finances.calc_takehome()
expense_table = build_expense_table()


print("\nExpected monthly takehome: {}\n".format(finances.calc_takehome()/12))
print("Expenses: \n{} \n expense total: {}\n\n".format(expense_table.loc[:,:], np.sum(expense_table.loc[:, 'monthly_total'])))
print("Discretionary monthly income: {}".format(finances.calc_discretionary_income(expense_table, finances.calc_takehome()/12)))

# Test input in terminal:
"""
100000, 40000, 0.05, mfj
car, 310
y
rent, 1200
y
food, 350
y
gas, 150
y
pets, 80
n
"""
