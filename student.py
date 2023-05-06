class Student:
    name="Elizabeth"
    age=23
    school="AkiraChix"
    nationality="Kenya"
    
# instance variables
# we may want to create where each objet of that class has its own unique values
# to do that we add an image method while defining the class
class Student:
    school="AkiraChix"
    def __init__(self,name,age,nationality):
        self.name = name                       #instance vriables
        self.age = age
        self.nationality=nationality
        
        
# Class methods
# methods add behavior to classes and they operate from the class attribute
# to create methods we use normal python functions
class Student:
     school="AkiraChix"
     def __init__(self,name,age,nationality):
        self.name = name                      
        self.age = age
        self.nationality=nationality
        
     def greet_student(self):
         return (f"Hello {self.name} welcome to {self.school}")
       
     def year_of_birth(self):
         year=2023 - self.age
         return (f"Hello {self.name} you are born in {year}")
     
     
    #  Assignments
    
    # No1
#  Update the Student Class to include these attributes - first_name, last_name, age, country
    #  - Add these methods to the Student class
    #          - show_full_name
    #          - year_of_birth
    #          - show_initials
    
class Student:
     school="AkiraChix"
     def __init__(self,first_name,last_name,age,country):
        self.first_name = first_name 
        self.last_name = last_name                       
        self.age = age
        self.country=country
        
     def show_full_name(self):
         return (f"my name is {self.first_name} {self.last_name}")
     
     def year_of_birth(self,year):
         current_year=year - self.age
         return (f"Hello {self.first_name} you are born in {current_year}")
     
     def show_initials(self):
         return(f"Hello my name starts with {self.first_name[0]} & {self.last_name[0]}")
     
    
    

     
         
    
    
         
        
        
        
        
        
        
     
