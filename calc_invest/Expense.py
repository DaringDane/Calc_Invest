class Expense:
    # Might need overhaul
    def __init__(self, total, frequency, has_interest=False):
        """
        Parent class of both fixed and interest-based expenses to be used for total earning and investment calculations

        Attributes:
            total (float) represents total amount of expense per transaction
            frequency (int) represents number of payments per month
            has_interest (bool) does expense have interest, or is it a fixed expense
        """
        self.total = total
        self.frequency = frequency
        self.has_interest = has_interest
    
    def monthly_cost(self):
        # Might need to put into child classes rather than parent class
        """
        Calculates and returns the monthly cost of an expense
        
        Args:
            None
        
        Returns:
            float: approximate monthly cost
        """
        monthly_cost= 1.0 * total * frequency
        return monthly_cost
    
    def adjust_cost(self, adjust):
        # write function to adjust costs that will integrate with fixed or interest expenses
        