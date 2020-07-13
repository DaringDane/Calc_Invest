import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#from .Expense import Expense


class Investment_Snapshot:
    
    def __init__(self, 
                 annual_taxable_income, 
                 current_investments, 
                 expected_pct_dividends, 
                 min_living_cost, 
                 filing_status='single'
                 ):
        
        """
        Overview of current investment/income situation for calculated projections of income and investment
        
        Args:
            annual_taxable_income (float) Income of all contributing individuals before tax
            current_investments (float) total of current investments
            expected_pct_dividends (float) average expected pct yield from present and future investments (decimal)
            min_living_cost (float) minimum annual new income user will accept living on
            filing_status (str) tax filing status (default 'single')
                - ['single', 'mfj', 'mfs', 'hoh'] - mfj = married, filing jointly, mfs = married, filing separately, hoh = head of household
        """
        self.income = annual_taxable_income
        self.current_investments = current_investments
        self.expected_pct_dividends = expected_pct_dividends
        self.min_living_cost = min_living_cost / 12 # monthly
        self.filing_status = filing_status
        
        
        
    def calc_takehome(self, 
                      brackets = [0.1, 0.12, 0.22, 0.24, 0.32, 0.35, 0.37], \
                      single = [9875, 40125, 85525, 163300, 207350, 518400], \
                      mar_joint = [19750, 80250, 171050, 326600, 414700, 622050], \
                      mar_sep = [9875, 40125, 85525, 163300, 207350, 311026], \
                      headoh = [14100, 53700, 85500, 163300, 207350, 518400]
                      ):
        """
        Constructs tax bracket table, sorts person into correct tax bracket, and monthly takehome after tax
        
        Args:
            brackets (list of floats) current tax bracket percentages
            single (list of floats) current single upper income thresholds for tax bracket
            mar_joint (list of floats) current married, filing jointly upper income thresholds for tax bracket
            mar_sep (list of floats) current married, filing separately upper income thresholds for tax bracket
            headoh (list of floats) current head of household upper income thresholds for tax bracket
        Returns:
            monthly net income after tax is withdrawn
        """
        ### updated with tax withholdings for 2021
        
        filing_dict = {'single':single, 'mfj':mar_joint, 'mfs':mar_sep, 'hoh':headoh}
        filing = filing_dict[self.filing_status]
        
        # return properly taxed income
        for i in range(1, len(filing)):
            if self.income <= filing[i - 1]:
                return self.income * (1.0 - brackets[i - 1]) / 12
            elif self.income <= filing[i] and self.income > filing[i - 1]:
                return self.income * (1.0 - brackets[i]) / 12
            else:
                return self.income * (1.0 - brackets[i + 1]) / 12
        
    def calc_discretionary_income(self, total_expenses, takehome, invest_dividends, pct_reinvest=0.7):
        
        """
        Takes into account expenses and income after tax to calculate discretionary income
            - to be used for further calculation of spending/investment

        Args:
            total_expenses (float) value sum of all expenses of user
            takehome (float) net income after tax
            pct_reinvest (float) decimal percent of monthly takehome to reinvest each month
            invest_dividents (float) expected dividend yield from current investments
        Returns:
            for_user_money (float): user spendable monthly income
            to_invest (float): amount of takehome to be invested
        """

        if total_expenses >= self.min_living_cost:
            print("Your expenses outstrip your desired living income. Consider reevaluating your priorities and your plan for places to cut down to make room for investment.")
            exit()
        
        else:
            for_user_money = self.min_living_cost - total_expenses
            for_user_money += invest_dividends * (1.0 - pct_reinvest) # add diff of pct divident funds chosen by user to discretionary spending
            to_invest = takehome - self.min_living_cost
            to_invest += invest_dividends * pct_reinvest # add pct of dividend funds chosen by user to reinvestment

        return for_user_money, to_invest


    if __name__ == '__main__':
        main()