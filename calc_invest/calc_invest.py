import pandas as pd
import numpy as np

from build_tables import build_expense_table
from Investment import Investment_Snapshot

def calc_invest():
    print("This is intended to maximize your investment portfolio along with quality of life, and focuses more on your future than your present. Sacrifice in the short term will yield comfort in the long term. \n")

    finance_base = input("Enter annual taxable income, current investment totals, expected pct dividends from investments(decimal), minimum net income you're able/willing to get by with, and tax filing status(single = single, mfj = married, filing jointly, mfs = married, filing separately, hoh = head of households): ").split(', ')
    print("Portfolio Started! Collecting more information...\n\n")

    bday = pd.to_datetime(input("Type in your birthday (MM/DD/YYYY): ")).date()
    today = pd.datetime.now().date()
    age = today.year - bday.year if bday.month < today.month else today.year - bday.year - 1

    retirement = int(input("How old would you like to be when you retire: "))
    retire_date = pd.to_datetime(f"{bday.month}, {bday.day}, {(retirement - age) + today.year}").date()

    months_remaining = month_difference(retire_date, today)

    annual_taxable_income, current_investments, expected_pct_dividends, min_living_cost, filing_status = \
        float(finance_base[0]), float(finance_base[1]), float(finance_base[2]), float(finance_base[3]), str(finance_base[4])

    finances = Investment_Snapshot(annual_taxable_income, current_investments, expected_pct_dividends, min_living_cost, filing_status)

    # create a table of expenses from user input
    expense_table = build_expense_table()
    # calc total expenses per month
    total_expenses = np.sum(expense_table[expense_table.columns[1]])
    dividends = finances.current_investments * (finances.expected_pct_dividends / 12) # assumes monthly dividends
    # uses investment_snapshot object to calculate after tax income/month
    net_takehome = finances.calc_takehome()

    # create list to store investment portfolio totals every month
    investment_totals = []
    discretionary_spending = []
    for _ in range(months_remaining):
        for_user_money, to_invest = finances.calc_discretionary_income(total_expenses, net_takehome, dividends, pct_reinvest=0.8)

        investment_totals.append(finances.current_investments)
        discretionary_spending.append(for_user_money)

        finances.current_investments += to_invest
        dividends = finances.current_investments * (finances.expected_pct_dividends / 12) # assumes monthly dividends

    print("All done! Run the following command in a jupyter notebook to see the effects on total income every year: \n data.groupby('year')[['total_for_you_income', 'discretionary_income']].sum()")
    print("You may need to increase max viewable rows. While n = your desired number of rows, use this command: \n pd.set_option('display.max_rows', n)")
    data = pd.DataFrame({'investment':investment_totals, 'discretionary_income':discretionary_spending, 'expenses':[int(total_expenses) for _ in range(len(investment_totals))]})
    data['investment'], data['discretionary_income'] = round(data['investment']).astype('int64'), round(data['discretionary_income']).astype('int64')
    data['total_for_you_income'] = data.discretionary_income + data.expenses
    data['year'] = [1 + (x // 12) for x in range(len(data))]
    return data


    # Test input in terminal:
"""
100000, 40000, 0.05, mfj
02/08/1992
70
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

# takes to dt objects and returns the months between the dates
def month_difference(a, b):
    return 12 * (a.year - b.year) + (a.month - b.month)