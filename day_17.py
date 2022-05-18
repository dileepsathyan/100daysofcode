import re

# RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.
# RegEx can be used to check if a string contains the specified search pattern.
# Python has a built-in package called re, which can be used to work with Regular Expressions.


# The re module offers a set of functions that allows us to search a string for a match:

# Function	    Description
# findall	    Returns a list containing all matches
# search	    Returns a Match object if there is a match anywhere in the string
# split	        Returns a list where the string has been split at each match
# sub	        Replaces one or many matches with a string


# Try using the search method in re.
txt1 = 'He passed in IELTS Exam'

x = re.search('^He.*Exam$', txt1)
# if x:
#     print('We have a match!')
# else:
#     print('No match...')



# Try using the findall method in re.
txt2 = 'Cups and Dips'
y = re.findall('ps', txt2)
# print(y)

# findall function returns and empty list if there is no match.
# print(re.findall('us', txt2))



# The split() function returns a list where the string has been split at each match
s = re.split(' ', txt2)
print(s)

# In the above method, if we have to split the string at the first white-space character:
t = re.split(' ', txt2, maxsplit=1)
print(t)









# Character	Description	                    Example	
# []	    A set of characters	            "[a-m]"
# \	        Signals a special sequence (can also be used to escape special characters)	"\d"
# .	        Any character (except newline character)	"he..o"
# ^	        Starts with	                    "^hello"
# $	        Ends with	                    "planet$"
# *	        Zero or more occurrences	    "he.*o"
# +	        One or more occurrences	        "he.+o"
# ?	        Zero or one occurrences	        "he.?o"
# {}	    Exactly the specified number of occurrences	"he.{2}o"
# |	        Either or	                    "falls|stays"



