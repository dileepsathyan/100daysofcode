import pandas as pd

# LAMBDA FUNCTIONS

# Lambda functions are usually small anonymous functions which takes any number of arguments but only 1 expression.
# These functions are powerful when combined with other functions.

# Syntax of Lambda functions

lambda argument : expression 


# Create a lambda function to add 10 to a given argument

func1 = lambda a : a+10

print(func1(5))