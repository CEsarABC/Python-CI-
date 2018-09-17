# this is a list

names = ['cesar', 'pablo', 'roger', 'jason', 'gabi', 'nicolas', 'kit']

print(names[2:4])
print(names[::2])

del names[0]
print(names)

names.insert(0, 'jhon')

print(names)

names.insert(4, 'ray')

print(names)

names.append('oscar')

print(names)

# .sort() function will sort alphabetically the items
names.sort()

print(names)
print('\n')

del names[3]
del names[0]

print(names)