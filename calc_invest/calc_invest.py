import pandas as pd
import numpy as np

from build_tables import build_expense_table
from Investment import Investment_Snapshot

print("This is intended to maximize your investment portfolio along with quality of life, and focuses more on your future than your present. Sacrifice in the short term will yield comfort in the long term. \n")

finance_base = input("Enter annual taxable income, current investment totals, expected pct dividends from investments(decimal), minimum net income you're able/willing to get by with, and tax filing status(single = single, mfj = married, filing jointly, mfs = married, filing separately, hoh = head of households): ").split(', ')
print("Portfolio Started! Collecting more information...\n\n")

bday = pd.to_datetime(input("Type in your birthday (MM/DD/YYYY): ")).date()
today = pd.datetime.now().date()
age = today.year - bday.year if bday.month < today.month else today.year - bday.year - 1

retirement = int(input("How old would you like to be when you retire: "))
retire_date = pd.to_datetime(f"{bday.month}, {bday.day}, {(retirement - age) + bday.year}").date()

# takes to dt objects and returns the months between the dates
def month_difference(a, b):
    return 12 * (a.year - b.year) + (a.month - b.month)

months_remaining = month_difference(retire_date, today)

annual_taxable_income, current_investments, expected_pct_dividends, min_living_cost, filing_status = \
    float(finance_base[0]), float(finance_base[1]), float(finance_base[2]), float(finance_base[3]), str(finance_base[4])

finances = Investment_Snapshot(annual_taxable_income, current_investments, expected_pct_dividends, min_living_cost, filing_status)


expense_table = build_expense_table()
dividends = finances.current_investments * finances.expected_pct_dividends
net_takehome = finances.calc_takehome()/12

# create list to store investment portfolio totals every month
investment_totals = []
discretionary_spending = []
for _ in months_remaining:
    for_user_money, to_invest = finances.calc_discretionary_income(expense_table, net_takehome, dividends, pct_invest=0.7)

    investment_totals.append(finances.current_investments)
    discretionary_spending.append(for_user_money)

    finances.current_investments += to_invest
    dividends = finances.current_investments * finances.expected_pct_dividends



# ADD AGGREGATION OF YEARLY PERSONAL INCOME 


print("\nExpected monthly takehome: {}\n".format(finances.calc_takehome()/12))
print("Expenses: \n{} \n expense total: {}\n\n".format(expense_table.loc[:,:], np.sum(expense_table.loc[:, 'monthly_total'])))
print("Discretionary monthly income: {}".format(finances.calc_discretionary_income(expense_table, finances.calc_takehome()/12, 0.7)))

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
