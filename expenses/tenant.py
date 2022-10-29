from expense import Expense


class Tenant:
    """
    Class that define a tenant properties
    name (str) : first name of tenant
    last_name (str) : last name of tenant
    building (str) : building name 
    floor (int) : number of floor
    current_month (int) : expenses for this month -> default 0
    last_balance (int) : expenses that tenant didn't paid -> default 0
    total_balance (int) : sum between current_month and total_balance -> default 0
    """


    def __init__(self, name, last_name, building, floor, current_month=0, last_balance=0, expenses = []):

        self.name = name
        self.last_name = last_name
        self.building = building
        self.floor = floor
        self.current_month = current_month
        self.last_balance = last_balance
        self.expenses = expenses
        self.total_balance = None
    
    def __str__(self):
        """
        Print info of tenant 
        """
        return f" name: {self.name}, last_name: {self.last_name}, building: {self.building}, floor: {self.floor}, current_month: {self.current_month}, last_balance: {self.last_balance}, total_balance: {self.total_balance} , expenses : {self.expenses}"  

    def __repr__(self):
        return str(self)

    def calc_total_balance(self):
        """
        calculate total balance with current month 
        and last balance
        """
        self.total_balance = self.current_month + self.last_balance

    def delete_tenant_info(self):
        """
        delete all data from the tenant to store new data
        without expenses array
        """
        self.name = ""
        self.last_name = ""
        self.building = ""
        self.floor = 0
        self.current_month = 0
        self.last_balance = 0
        self.total_balance = 0
