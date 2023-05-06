# #Create 3 files in the classes directory car.py, fruit.py, and bank.py.
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

class Car:
     wheels=4
     def __init__(self,make,model,color):
        self.make = make                      
        self.model = model
        self.color = color
        
     def start_car(self):
         return (f"vooom voom")
     
     def car_capacities(self,capacity):
         return(f"My {self.color} {self.make} {self.model} carries {capacity} people")
     
     def car_price(self,price):
         return(f"my {self.color} {self.make} {self.model} cost {price}")
     

        