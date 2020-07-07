class Expense:
    # Might need overhaul
    def __init__(self, name, monthly_total):
        """
        Parent class of both fixed and interest-based expenses to be used for total earning and investment calculations

        Attributes:
            name (str)
            monthly_total (float) represents total amount of expense per month
        """
        # potential att: has_interest (bool) does expense have interest, or is it a fixed expense
        # self.has_interest = has_interest
        self.name = name
        self.monthly_total = monthly_total
        

    