import sys
sys.path.append(".")
from expenses.expense import Expense
from expenses.consortium import Consortium
from expenses.tenant import Tenant


class Expenses_Page:
    def __init__(self):
        self.tenant = None
        self.consortium = None
        self.expenses = []

    def add_expense(self, name, expense_variable, value):
        """
        Create Expenses array data using Expense Class
        """
        self.expenses.append(Expense(name, expense_variable, value))

    def add_consortium(self, name, address, phone, mail):
        """
        Create Consortium object data using Consortium Class
        """
        self.consortium = Consortium(name, address, phone, mail)

    def add_tenant(self, name, last_name, building, floor, current_month=0, last_balance=0):
        """
        Create Tenant object data using Tenant Class
        """
        self.tenant = Tenant(name, last_name, building, floor, current_month, last_balance)
        self.tenant.calc_total_balance()

    def __str__(self) -> str:
        """
        Print info of tenant 
        """
        return f"consortium: {self.consortium}, expenses : {self.expenses}, tenant : {self.tenant}"  


# create class
# test = Expenses_Page()
# # add expenses
# test.add_expense('Tasa municipal', 'city_tax', 400)
# test.add_expense('Tasa inmobiliaria', 'real_state_tax', 400)
# # add consortium data
# test.add_consortium('Adm. Lares', 'Santa Fe 6700. Rosario, Santa Fe, AR', '3413657899', 'adm_lares@lares.com')
# # add tenant
# test.add_tenant('Hernan', 'Gobu', 'Heras 5', 7, 35, 0)

# print(test)