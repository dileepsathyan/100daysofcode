import pandas as pd

# LAMBDA FUNCTIONS

# Lambda functions are usually small anonymous functions which takes any number of arguments but only 1 expression.
# These functions are powerful when combined with other functions.

# Syntax of Lambda functions

lambda argument : expression 


# Create a lambda function to add 10 to one argument
func1 = lambda a : a+10
# print(func1(5))


# Create a lambda function with 2 arguments
func2 = lambda a, b : a*b
# print(func2(2, 4))


# Create a lambda function with 3 arguments
func3 = lambda a, b, c: (a + b)**c
# print(func3(3, 4, 2))

# Create a default lambda function and reuse it to create more functions.
def func4(n):
    return lambda a: a * n

func5_doubler = func4(2)
func6_tripler = func4(3)
# print(func5_doubler(4))
# print(func6_tripler(7))

#####################################################################################################################

# CLASSES AND OBJECTS

# A Class is like an object constructor, or a "blueprint" for creating objects.

# Create a Class with 1 property called x
# Then assign the class to p1 to call the property from p1

class my_first_class:
    x = 10
    y = 63
    z = 246

p1 = my_first_class()
# print(p1.x)
# print(p1.y)
# print(p1.z)



# The __init__() function

# The examples above are classes and objects in their simplest form, and are not really useful in real life applications.
# To understand the meaning of classes we have to understand the built-in __init__() function.
# All classes have a function called __init__(), which is always executed when the class is being initiated.
# Use the __init__() function to assign values to object properties, or other operations that are necessary to do when the object is being created:

# Create a class and assign values using __init__ function.

class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

p2 = Person('Dileep', 30, 'Male')
# print(p2.name)
# print(p2.age)
# print(p2.gender)


# Object Methods: Objects can also contain methods. Methods in objects are functions that belong to the object.

class HelloPerson:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = str(age)
        self.gender = gender
    
    def say_hello(self):
        print('Hello Mr. ' + self.name + ', You are a ' + self.gender + ' of age ' + self.age + ' years')
    
# p3 = HelloPerson('Dileep', 30, 'Male')
# print(p3.say_hello())


# The self Parameter
# The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.
# It does not have to be named self , you can call it whatever you like, but it has to be the first parameter of any function in the class.

class HelloPerson:
    def __init__(can_be_anything, name, age, gender):
        can_be_anything.name = name
        can_be_anything.age = str(age)
        can_be_anything.gender = gender
    
    def say_hello(this_too_can_be_different):
        print('Hello Mr. ' + this_too_can_be_different.name)
    
# p4 = HelloPerson('Dileep', 30, 'Male')
# print(p4.say_hello())



# Modify Object Properties
p3.age = 34

# Delete Object Properties
del p3.name

# Delete Objects
del p4