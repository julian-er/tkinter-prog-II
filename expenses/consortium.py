class Consortium:
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

    def __init__(self, name, address, phone, mail):

        self.name = name
        self.address = address
        self.phone = phone
        self.mail = mail

    
    def __str__(self):
        """
        Print info of tenant 
        """
        return f" name: {self.name}, address: {self.address}, phone: {self.phone}, mail: {self.mail}"  
    
    def __repr__(self):
        return str(self)

