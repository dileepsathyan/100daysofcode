import pandas as pd


# INHERITANCE

# Inheritance allows us to define a class that inherits all the methods and properties from another class.
# Parent class is the class being inherited from, also called base class.
# Child class is the class that inherits from another class, also called derived class.

# Create a Parent Class

class Parent:
    def __init__(self, first_name, last_name):
        self.fname = first_name
        self.lname = last_name
    
    def print_name(self):
        print('Hi, '+ self.fname, self.lname + '!..')

p1 = Parent('Dileep', 'Sathyan')
p1.print_name()    
