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

# p1 = Parent('Dileep', 'Sathyan')
# p1.print_name()    



# Create a child class
# To create a class that inherits the functionality from another class, send the parent class as a parameter when creating the child class.

class Student(Parent):
    pass

# p2 = Student('Trinay', 'Dileep')
# p2.print_name() 



# Adding __init__() function overrides the inheritance of the parent's __init__() function.
# This means, when you add the __init__() function, the child class will no longer inherit the parent's __init__() function.

class Student1(Parent):
    def __init__(self, first_name, last_name):
        # add new properties here



# To keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function as below.

class Student2(Parent):
    def __init__(self, first_name, last_name):
        Parent.__init__(self, first_name, last_name)

p3 = Student2('Dileep', 'Trinay')
p3.print_name()
