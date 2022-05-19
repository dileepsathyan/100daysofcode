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


    