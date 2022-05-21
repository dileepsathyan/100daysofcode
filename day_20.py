# While Loops

# A while loop executes a set of statements as long as a condition is true.
# The while loop requires relevant variables to be ready, in the below example we need to define an indexing variable, i, which we set to 1 intially.
i = 1
while i <= 5:
    print(i)
    i += 1



# Break statement helps stop the loop even if the while condition is true:
j = 10
while j < 15:
    print(j)
    if j == 13:
        break
    j +=1



# Continue statement helps stop the current iteration and continue with the next one.
k = 0
while k < 5:
    k += 1
    if k == 4:
        continue
    print(k)


# Else statement can help run a block of code when a condition is no longer true.
l = 1
while l < 5:
    print(l)
    l += 1
else:
    print('l is no longer less than 5')



# For loops
# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

