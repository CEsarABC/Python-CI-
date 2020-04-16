person_1 = {
'name' : 'cesar',
'age': 23,
'job': 'programer'}

print(person_1['name'])

numbers = {
1 : 'one',
2 : 'two',
3 : 'three'
}

print( 1 in numbers)
print( 5 in numbers)
print(numbers.get(5,'not found'))
print(numbers.get(3,'not found'))
