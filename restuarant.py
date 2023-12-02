# Restaurant __init__()`
# - Restaurants should be initialized with a name, as a string
#- `Restaurant name()`
# - returns the restaurant's name
#- should not be able to change after the restaurant is created

#`  Restaurant reviews()`
 # -returns a list of all reviews for that restaurant
#- `Restaurant customers()`
 # -Returns a **unique** list of all customers who have reviewed a particular restaurant.


class Restuarant():
    def __init__(self,restuarant_name): #initialized the restuarant with a name
        self._restuarant_name=restuarant_name
        self.reviews=[] #stores the reviews associated with the restuarant 
