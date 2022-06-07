persons = ['Dileep', 'Sachu', 'Trinay', 'Sathyan', 'Latha']
age = [34, 32, 4, 65, 61]

combined = zip(persons, age)
# print(list(combined))


result = [('Dileep', 34), ('Sachu', 32), ('Trinay', 4), ('Sathyan', 65), ('Latha', 61)]

unzipped = list(zip(*result))
# print(unzipped)

for i in unzipped:
    print(list(i))


ind = zip(range(5), persons)
# print(list(ind))

for i, item in list(ind):
    print(i)