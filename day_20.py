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

# Looping through a list
fruits = ['apple', 'banana', 'guava']
for i in fruits:
    print(i)



# Looping through a string
word = 'apples'
for i in word:
    print(i)



# Break statement in for loops
fruits = ['apple', 'banana', 'guava']
for i in fruits:
    print(i)
    if i == 'banana':
        break



# Continue statement stops the current iteration and continues the next one
fruits = ['apple', 'banana', 'guava']
for i in fruits:
    if i == 'banana':
        continue
    print(i)



# range() functions is used to loop through a set of code a specified number of times.
for i in range(6):
    print(i)


# Use the start parameter in range() function:
for i in range(2,6):
    print(i)


# Use the increment sequence constomiser in the range() function.
for i in range(1, 9, 2):
    print(i)


# Else statement in a for loop is used to execute a block of code when the iteration is over.
for i in range(1, 6):
    print(i)
else:
    print('Printed from 1 to 5...')



# Break function is used to stop the loop based on a condition.
for i in range(6):
    if i == 4: break
    print(i)


# A nested loop is a loop inside a loop.
# The "inner loop" will be executed one time for each iteration of the "outer loop"
qty = [3, 5]
item = ['car', 'fruits', 'house', 'persons']
for q in qty:
    for i in item:
        print(q, i)


# for loops cannot be empty, but if you for some reason have a for loop with no content, put in the pass statement to avoid getting an error.
for i in range(6):
    pass
