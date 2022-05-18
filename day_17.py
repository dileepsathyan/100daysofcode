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
# print(s)

# In the above method, if we have to split the string at the first white-space character:
t = re.split(' ', txt2, maxsplit=1)
# print(t)



# The sub() function substitutes the matches with the text of your choice:
u = re.sub('s', 'z', txt2)
# print(u)



# A Match Object is an object containing information about the search and the result.
# The below returns a match object
m = re.search('am', txt1)
# print(m)


# The Match object has properties and methods used to retrieve information about the search, and the result:
# .span() returns a tuple containing the start-, and end positions of the match.
# .string returns the string passed into the function
# .group() returns the part of the string where there was a match

print(m.span)
print(m.string)
print(m.group())




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



# A special sequence is a \ followed by one of the characters in the list below, and has a special meaning:

# Character	Description	                                                                                    Example	
# \A	    Returns a match if the specified characters are at the beginning of the string	                "\AThe"	 
# \b	    Returns a match where the specified characters are at the beginning or at the end of a word     r"ain\b"
#           (the "r" in the beginning is making sure that the string is being treated as a "raw string")	r"\bain"
# \B	    Returns a match where the specified characters are present, but NOT at the beginning (or at the end) of a word  r"ain\B"
#           (the "r" in the beginning is making sure that the string is being treated as a "raw string")	r"\Bain"
# \d	    Returns a match where the string contains digits (numbers from 0-9)	                            "\d"	 
# \D	    Returns a match where the string DOES NOT contain digits	                                    "\D"	 
# \s	    Returns a match where the string contains a white space character	                            "\s"	 
# \S	    Returns a match where the string DOES NOT contain a white space character	                    "\S"	 
# \w	    Returns a match where the string contains any word characters (characters from a to Z, digits from 0-9, and the underscore _ character)	"\w"	 »
# \W	    Returns a match where the string DOES NOT contain any word characters	                        "\W"	 
# \Z	    Returns a match if the specified characters are at the end of the string	                    "Spain\Z"



