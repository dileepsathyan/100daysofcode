from cgi import print_environ_usage
import pandas as pd


# A function is a set of code that performs any given task, enabling the programmer to modularize a program. 
# All variables created in function definitions are local variables; they are known only to the function in which they are declared.


# Basic Function syntax
def new_function():
    print('This is the basic function syntax')

new_function()


## Types of arguments in Python functions

# 1. Default arguments
# Functions can be defined with default arguments. If the values for the arguments are not supplied when the function is called, the default argument is used.

def default_arg_function(item = 'an empty box'):
    print('This is ' + item)

default_arg_function('apple')
default_arg_function()
default_arg_function('banana')


# 2. Arbitrary arguments
# Arbitrary arguments are used when you want the function to take an unlimited number of arguments. When you add an asterisk ( * ), it will receive a tuple of arguments.

def arb_function(*args):
    print(args)

arb_function(1, 2, 3, 4)


# We can explicitly return a value in the arguments as below.
def arb_function1(*args):
    print(args[3])

arb_function1('Dog', 'Cat', 'Monkey', 'Bird')



# 3. Keyword arguments
# You can pass the arguments in a non-positional manner using keyword arguments as below.

def keyword_arg_function(name, age):
    print(name + ' is ' + str(age) + ' years old.')

keyword_arg_function(name='Dileep', age=30)


# The Return Statement in Python Functions.
# To return a value from a function, we use a return statement. It “returns” the result to the caller.
# If a user doesn’t include a return statement, it returns None

def sum_of_2_nums(a, b):
    return a + b

print(sum_of_2_nums(120, 30))


# Nested functions
# A nested function is a function that is defined inside another function—it is also called an inner function. 
# One of the main reasons to use nested functions is to prevent the data or functionality from being accessed by other parts of the code.

qty = [10, 21, 25]
pdt = ['cars', 'bikes', 'aeroplanes']
for i in qty:
    for j in pdt:
        print(i, j)


# Recursive Function
# A recursive function is a function that repeats its behavior until a specified condition is met.

def rec_function(num):
    if num == 10:
        print(num)
        print('Process Complete...')
    else:
        print(num)
        rec_function(num+1)

rec_function(6)