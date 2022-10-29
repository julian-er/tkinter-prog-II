from expenses_classes.service import Service


class Consortium:
    """
    Class that define a tenant properties
    name (str) : first name of tenant
    last_name (str) : last name of tenant
    building (str) : building name 
    """

    def __init__(self, name, address, phone, mail, cuit, cbu, bank_branch, account_holder):

        self.name = name
        self.address = address
        self.phone = phone
        self.mail = mail
        self.cuit = cuit
        self.cbu = cbu
        self.bank_branch = bank_branch
        self.account_holder = account_holder
        self.services = []

    def add_service(self, service_variable, value):
        """
        Create Expenses array data using Expense Class
        """
        self.services.append(Service(service_variable, value))

    def __str__(self):
        """
        Print info of tenant 
        """
        return f" name: {self.name}, address: {self.address}, phone: {self.phone}, mail: {self.mail}, cuit: {self.cuit}, cbu: {self.cbu}, bank_branch:{self.bank_branch}, ac_holder:{self.account_holder}, services :{self.services}"

    def __repr__(self):
        return str(self)

#test
# test = Consortium('juan', 'sarasa', 'djkalsjdlksa', '840983209','dsadsa', 'dsadsa', 'dsadasd', '0dasdasd')
# test.add_service('locksmith_phone', '7676767676')
# print(test)
