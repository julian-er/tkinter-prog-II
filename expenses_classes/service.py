class Service:
    """
    Class that define a services of consortium properties
    service_variable(str) : name of the expense variable
    value (str) : any info of this service 
    """

    def __init__(self, service_variable, value):

        self.service_variable = service_variable
        self.value = value
    
    def __str__(self):
        """
        Print info of service
        """
        return f"[expense_variable: {self.service_variable}, value: {self.value}]"  
    
    def __repr__(self):
        return str(self)
