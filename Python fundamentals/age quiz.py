age = int(input('Enter your age: '))

if age < 0:
    print('Sorry. I can’t tell what drink because that age is incorrect!')
elif age < 14:
    print('Drink Toddy')
elif age < 18:
    print('Drink Coke')
elif age < 21:
    print('Drink beer')
elif age < 130:
    print('Drink whisky')
else:
    print('Sorry. I can’t tell what drink because that age is incorrect!')