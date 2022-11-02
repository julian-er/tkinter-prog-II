#  this file is not in use right now 
class Expense:
    """
    Class that define a expense properties
    name (str) : name of the expense 
    expense_variable(str) : name of the expense variable
    value (int) : number of the cost
    """

    def __init__(self, expense_variable, value):

        self.expense_values = {expense_variable : value}
        # self.value = value
    
    def __str__(self):
        """
        Print info of expense
        """
        # return f"[expense_variable: {self.expense_variable}, value: {self.value}]"  
        return f"{self.expense_values}"  
    
    def __repr__(self):
        return str(self)
