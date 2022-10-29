class Expense:
    """
    Class that define a expense properties
    name (str) : name of the expense 
    expense_variable(str) : name of the expense variable
    value (int) : number of the cost
    """

    def __init__(self, name, expense_variable, value):

        self.name = name
        self.expense_variable = expense_variable
        self.value = value
    
    def __str__(self):
        """
        Print info of tenant 
        """
        return f"[expense: {self.name}, expense_variable: {self.expense_variable}, value: {self.value}]"  
    
    def __repr__(self):
        return str(self)
