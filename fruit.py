## #Create 3 files in the classes directory car.py, fruit.py, and bank.py.
# Define the following classes in each module respectively. 
# Car
# Fruit
# Account
# Each class should have one class attribute and three instance variables.

# Discuss in your group and come up with the attributes and 
# three methods (behaviours) for each class and implement them

# Then do the following in the interpreter 
# Create two instances of each class. 
# Call each of the methods you defined.
# Once you verify all the methods are working, commit your work, push to GitHub and submit. 

class Fruits:
     nutrient="Vitamins"
     def __init__(self,name,color,taste):
        self.name = name                      
        self.color = color
        self.taste =taste
        
     def fruits_price(self,price):
         return (f"i bought {self.color} {self.taste} {self.name} at {price} shillings")
     
     def fruits_expiry_date(self,date):
         return(f"my {self.taste} {self.color} {self.name} will expire on {date} may 2022")
     
     def fruits_shape(self,shape):
         return(f"i bought {self.taste} {self.color} {shape} {self.name} yesterday")