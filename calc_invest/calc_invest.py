import pandas as pd
import numpy as np

from build_tables import build_expense_table
from Investment import Investment_Snapshot

def calc_invest(
    annual_taxable_income,
    current_investments,
    expected_pct_dividends,
    min_living_cost,
    filing_status,
    pct_reinvest,
    months_remaining=0,
    expense_table=None
    ):
    """
    Takes basic income and tax filing information from user to generate a financial portfolio with modifiable variables and projections until retirement

    Args:
    annual_taxable_income (float): total pre-tax income as entered in tax filing
    current_investments (float): total current investments
    expected_pct_dividends (float): average annual return on investments as a float (i.e. - 0.05 = 5%)
    min_living_cost (float): minimum acceptable living cost user is willing to accept - used for calculations of reinvestment income distribution
        ['single', 'mfj', 'mfs', 'hoh'] - mfj = married, filing jointly, mfs = married, filing separately, hoh = head of household
    filing_status (string): tax filing status - used to calculate after-tax income
    pct_reinvest (float): float percentage of dividend payments to automatically reinvest
    months_remaining (int): months until retirement. If empty, user is prompted to input data to generate retirement data
    expense_table (pandas DF): table with 2 attributes - expense name and monthly cost. Can pass in df from external .csv or other file

    Returns:
    Dataframe with monthly investment totals and personal spending totals from present until desired retirement age
    """

    print("This is intended to maximize your investment portfolio along with quality of life, and focuses more on your future than your present. Sacrifice in the short term will yield comfort in the long term. \n")

    # finance_base = input("Enter annual taxable income, current investment totals, expected pct dividends from investments(decimal), minimum net income you're able/willing to get by with, and tax filing status(single = single, mfj = married, filing jointly, mfs = married, filing separately, hoh = head of households): ").split(', ')
    # print("Portfolio Started! Collecting more information...\n\n")

    if months_remaining == 0:
        months_remaining = time_till_retirement()

    # annual_taxable_income, current_investments, expected_pct_dividends, min_living_cost, filing_status = \
    #     float(finance_base[0]), float(finance_base[1]), float(finance_base[2]), float(finance_base[3]), str(finance_base[4])

    finances = Investment_Snapshot(annual_taxable_income, current_investments, expected_pct_dividends, min_living_cost, filing_status)

    # dict of args to return so user can reinitialize calculations with different parameters
    args_dict = dict(annual_taxable_income=annual_taxable_income, 
                    current_investments=current_investments, 
                    expected_pct_dividends=expected_pct_dividends, 
                    min_living_cost=min_living_cost, 
                    filing_status=filing_status,
                    pct_reinvest=pct_reinvest,
                    months_remaining=months_remaining
                    )

    # create a table of expenses from user input
    if expense_table is None:
        expense_table = build_expense_table()
    elif type(expense_table) is dict:
        expense_table = pd.DataFrame(expense_table)
    # calc total expenses per month
    total_expenses = np.sum(expense_table[expense_table.columns[1]])
    dividends = finances.current_investments * (finances.expected_pct_dividends / 12) # assumes monthly dividends
    # uses investment_snapshot object to calculate after tax income/month
    net_takehome = finances.calc_takehome()

    # create list to store investment portfolio totals every month
    investment_totals = []
    discretionary_spending = []
    for _ in range(months_remaining):
        for_user_money, to_invest = finances.calc_discretionary_income(total_expenses, 
                                                                       net_takehome, 
                                                                       dividends, 
                                                                       pct_reinvest)

        investment_totals.append(finances.current_investments)
        discretionary_spending.append(for_user_money)

        finances.current_investments += to_invest
        dividends = finances.current_investments * (finances.expected_pct_dividends / 12) # assumes monthly dividends

    data = pd.DataFrame({'investment':investment_totals, 'discretionary_income':discretionary_spending, 'expenses':[int(total_expenses) for _ in range(len(investment_totals))]})
    data['investment'], data['discretionary_income'] = round(data['investment']).astype('int64'), round(data['discretionary_income']).astype('int64')
    data['total_income'] = data.discretionary_income + data.expenses
    data['year'] = [1 + (x // 12) for x in range(len(data))]

    by_year_calc = data.groupby('year')[['total_income', 'discretionary_income']].sum
    plot_yearly = by_year_calc()
    plot_yearly['total_invested'] = data.groupby('year')['investment'].last()

    return data, plot_yearly, args_dict, expense_table


# takes to dt objects and returns the months between the dates
def month_difference(a, b):
    """
    Calculates difference in months between two datetime objects

    Args:
    a (pandas datetime object) latest datetime object
    b (pandas datetime object) earliest datetime object
    
    Returns:
    integer value of months between two dates
    """
    return 12 * (a.year - b.year) + (a.month - b.month)

def time_till_retirement():
    bday = pd.to_datetime(input("Type in your birthday (MM/DD/YYYY): ")).date()
    today = pd.datetime.now().date()
    age = today.year - bday.year if bday.month < today.month else today.year - bday.year - 1

    retirement = int(input("How old would you like to be when you retire: "))
    retire_date = pd.to_datetime(f"{today.month}, {today.day}, {(retirement - age) + today.year}").date()

    months_remaining = month_difference(retire_date, today)
    return months_remaining

def update(Args, new_values, args_dict):
    """
    Input list of arguments to modify and list of new values to replace old parameters
    NOTE: length of [Args] and [new_values] MUST be equal

    Args:
    Args (list of strings): list of names of arguments to modify
    new_values (list): list of values to modify strings
    args_dict (dict): hash table with parameters and values used for calculation

    Returns:
    updated dictionary of parameters for new investment calculation
    """
    for i in range(len(Args)):
        args_dict[Args[i]] = new_values[i]

    return args_dict


    # Test input in terminal:
"""
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