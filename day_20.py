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



