#testing the functionality
from customer import Customer
from restuarant import Restuarant
from review import Review


#output for customers
customer1 = Customer("Judy", "sigilai")
customer2 = Customer("Brian", "Kip")

print(customer1.full_name())  
print(customer2.full_name())
print(customer2.given_name())
print(customer2.family_name())
print(customer2.all()) #its a class method


#output for restuarant
restuarant1=Restuarant("Frangos")
restuarant2=Restuarant("The Curve")

print (restuarant1.name)
print (restuarant2.name)
