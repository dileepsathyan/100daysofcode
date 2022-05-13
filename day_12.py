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
print(func3(3, 4, 2))


