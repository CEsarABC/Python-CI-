heroes = ['Hulk', 'Wolverine', 'Batman', 'Spiderman', 'Superman', 'Gambit']
print(heroes)
numbers = [1,2,3,4,5]
print(numbers)

print(heroes[2])

heroes[3] = 'Psilock'
print(heroes[3])
print(heroes)

print('check if flash is in the list:')

if 'flash' in heroes:
    print('Flash is in the list')
else:
    print('Flash is not in the list')

print('check if Magneto is in the list:')

if 'Magneto' in heroes:
    print('Magneto is in the list')
else:
    print('Magneto is not in the list')

heroes = (heroes + ['Pyro', 'Cyclops'])
print(heroes)

# append insets one item at the end of the list

heroes.append('Jubilee')
heroes.append('Beast')
print(heroes)

print(len(heroes))

# insert will put an item in a particular place in the list

heroes.insert(1, 'Archangel')
print(heroes[1])
print(heroes)

# index shows the index number of the item
print(heroes.index('Superman'))
print(heroes.index('Pyro'))

