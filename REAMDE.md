# Investment Portfolio Calculator
_Purpose_: This python package creates a life snapshot of an individual or family and returns projections of their 
investment portfolio up till and beyond retirement (of their choice) and implement my personal model for distributing
investment funds, dividends, and personal spending funds that could provide someone working in a corporate environment
a roadmap to retiring comfortably. 

## Functionalities
1. Take a table of expenses with names, frequency of purchase, and whether or not payments have interest
associated, and generate monthly impact totals against their income
  a. If no table is provided, user is prompted to enter data which will automatically form a table

2. Have users input their __before tax salary__ and __tax filing status__, __amount of current investments__, 
__average expected % yield via dividends__ from all investments (very rough estimate), and __amount of dividends to reinvest
vs. apply to their discretionary income__. Calculations of after tax income and dividend reinvestment calculations take 
place, factoring in expense totals to yield _visualizations of projected investment/discretionary spending totals_.

3. Adjust variables of investment portfolio and compare outcomes in graphical form to make decisions on how to coordinate
investment resources long-term.

### Eventual Additions:
_RETURN_ whether a desired retirement outcome is possible with their current situation, and if it is, what the minimum 
necessary amount of investment is to maximize the money they could spend on themselves in attaining proper retirement savings.

## __Limitations__
* Relies on relatively accurate accounting of expenses by the user. 
* Does not accounts for average wage increases and inflation averages
* Assumes the same income for the duration of calculation. 
* Assumes a relatively stable economy - doesn't account for recessions, but an average over longer periods of time

## Instructions for Use:
  _Jupyter Notebook_
  This package is designed for jupyter notebooks because of the ease of visualization through that platform. 
  
  A jupyter notebook is provided in this repo with basic visualizations and a UI that allows the user to change
  all parameters of the investment portfolio and run it again immediately to see the difference in outcomes.






