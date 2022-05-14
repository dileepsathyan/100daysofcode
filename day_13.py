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

# s1 = Parent('Dileep', 'Sathyan')
# s1.print_name()    



# Create a child class
# To create a class that inherits the functionality from another class, send the parent class as a parameter when creating the child class.

class Student(Parent):
    pass

# s2 = Student('Trinay', 'Dileep')
# s2.print_name() 



# Adding __init__() function overrides the inheritance of the parent's __init__() function.
# This means, when you add the __init__() function, the child class will no longer inherit the parent's __init__() function.

class Student1(Parent):
    def __init__(self, first_name, last_name):
        # add new properties here
        pass



# To keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function as below.

class Student2(Parent):
    def __init__(self, first_name, last_name):
        Parent.__init__(self, first_name, last_name)

# s3 = Student2('Dileep', 'Trinay')
# s3.print_name()



# Use the super() Function
# Python also has a super() function that will make the child class inherit all the methods and properties from its parent:

class Student3(Parent):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.graduation_year = 2008

# s4 = Student3('Dileep', 'Trinay')
# print(s4.graduation_year)



# In the example below, the year 2019 should be a variable, and passed into the Student class when creating student objects. 
# To do so, add another parameter in the __init__() function.

class Student4(Parent):
    def __init__(self, first_name, last_name, year):
        super().__init__(first_name, last_name)
        self.graduation_year = year

s5 = Student4('Dileep', 'Trinay', 2008)
print(s5.graduation_year)
print(s5.fname)



# Add Methods to Child class

class Student5(Parent):
    def __init__(self, first_name, last_name, year):
        super().__init__(first_name, last_name)
        self.graduation_year = year

    def welcome(self):
        print('Welcome, '+ self.fname, self.lname)

s6 = Student5('Dileep', 'Trinay', 2008)
s6.welcome()