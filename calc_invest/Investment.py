import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from .FixedExpense import FixedExpense
from .InterestExpense import InterestExpense


class Investment_Snapshot:
    
    def __init__(self, annual_taxable_income, current_investments, expected_pct_dividends, filing_status='single', tax=0.12):
        
        """
        Overview of current investment/income situation for calculated projections of income and investment
        
        Args:
            annual_taxable_income (float) Income of all contributing individuals before tax
            current_investments (float) total of current investments
            expected_pct_dividends (float) average expected pct yield from present and future investments
            filing_status (str) tax filing status (default 'single')
                - ['single', 'married, filing jointly', 'married, filing separately', 'head of household']
            tax (float) tax percentage withheld from income (default 0.12)
        """
        self.income = annual_taxable_income
        self.investments = current_investments
        self.dividends = expected_pct_dividends
        self.filing_status = filing_status
        self.tax = tax
        
        
        
    def calc_mthly_takehome(self, brackets = [0.1, 0.12, 0.22, 0.24, 0.32, 0.35, 0.37], \
                            single = [9875, 40125, 85525, 163300, 207350, 518400], \
                            mar_joint = [19750, 80250, 171050, 326600, 414700, 622050] \
                            mar_sep = [9875, 40125, 85525, 163300, 207350, 311026] \
                            headoh = [14100, 53700, 85500, 163300, 207350, 518400]
                           ):
        
        """
        Constructs tax bracket table, sorts person into correct tax bracket, and calculates monthly takehome after tax
        
        Args:
            brackets (list of floats) current tax bracket percentages
            single (list of floats) current single upper income thresholds for tax bracket
            mar_joint (list of floats) current married, filing jointly upper income thresholds for tax bracket
            mar_sep (list of floats) current married, filing separately upper income thresholds for tax bracket
            headoh (list of floats) current head of household upper income thresholds for tax bracket
        """
        ### updated with tax withholdings for 2021
        
        filing_dict = {'single':single, 'married, filing jointly':mar_joint, 'married, filing separately':mar_sep, 'head of household':headoh}
        filing = filing_dict[self.filing_status]
        
        # return properly taxed income
        for i in range(1, len(filing)):
            if self.income <= filing[i - 1]:
                return np.divide(self.income * (1.0 - brackets[i - 1]), 12)
            elif self.income <= filing[i] and self.income > filing[i - 1]:
                return np.divide(self.income * (1.0 - brackets[i]), 12)
            else:
                return np.divide(self.income * (1.0 - brackets[i + 1]), 12)
        
    def calc_discretionary_income(self, cont=True, expense):
        
        """
        Takes into account expenses and income after tax to calculate discretionary income
        """