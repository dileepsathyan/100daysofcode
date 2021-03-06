from numpy import dtype

# Exception Handling in Python

# The try block lets you test a block of code for errors.
# The except block lets you handle the error.
# The else block lets you execute code when there is no error.
# The finally block lets you execute code, regardless of the result of the try- and except blocks.

# The try block will generate an exception, because x is not defined

try:
    print(x)
except:
    print('Variable x was not defined but the exception has been handled...')


# Many Exceptions: You can define as many exception blocks as you want.
# e.g. if you want to execute a special block of code for a special kind of error:

try:
    print(y)
except NameError:
    print('y is not defined..')
except:
    print('some other error occured..')


# Else: You can use the else keyword to define a block of code to be executed if no errors were raised.

try:
    print('Hi')
except:
    print('This is the except block..')
else:
    print('This is else block which means there are no errors found...')



# Finally: The finally block, if specified, will be executed regardless if the try block raises an error or not

try:
    print(x)
except:
    print('This is the except block because x was not defined..')
finally:
    print('This is finally block which will be exceuted no matter what')



# Raise an exception: As a Python developer you can choose to throw an exception if a condition occurs.
# To throw (or raise) an exception, use the raise keyword..

n = -1

if n < 0:
    raise Exception('No numbers below zero')
