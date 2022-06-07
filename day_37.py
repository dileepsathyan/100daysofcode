# Zip,  Unzip and Enumerate methods in Python.

name = ['John', 'Smith', 'Adam', 'Filipe', 'Steve']
age = [34, 32, 4, 65, 61]



# Zip both the name and age lists in 1 list.

zipped_list = list(zip(name, age))
# print(zipped_list)


# Unziping the zipped_list
zip_list = [('John', 34), ('Smith', 32), ('Adam', 4), ('Filipe', 65), ('Steve', 61)]

unzipped_list = list(zip(*zip_list))
# print(unzipped_list)


# Extract the values from the unzipped_list as separate lists
for i in unzipped_list:
    print(list(i))


# If we have to index the values in a list.
countries = ['India', 'USA', 'Canada', 'UAE', 'Australia']
