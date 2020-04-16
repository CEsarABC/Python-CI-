numbers = [0,1,2,3,4,5,6,7,8,9,10]

new_string = 'numbers {0}, {1}, {2}'.format(numbers[0],numbers[1],numbers[2])

print(new_string)

numbers = [2,11,20019]

new_string_date = 'Date: {0}/{1}/{2}'.format(numbers[0],numbers[1],numbers[2])

print(new_string_date)

x = '{z}/{y}'.format(z=100,y=200)

print(x)
print(type(x))

name = 'Amandine'

string_name = 'good morning {0}'.format(name)
print(string_name)

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))
