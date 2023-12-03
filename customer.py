from review import Review


class Customer:
    customers=[] #declaring a variable to hold the customers
    def __init__(self,first_name,last_name):
        self.first_name=first_name
        self.last_name=last_name
        self.customers.append(self) #appending each created instance to the list

        self.reviews=[] # used to store each customers review
    def given_name(self): #getter method used to retrieve the name
        return self.first_name
    def family_name(self):
        return self.last_name
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    