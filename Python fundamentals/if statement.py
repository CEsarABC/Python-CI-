print('if statement choosing options')
print('Amateur, Professional, Veteran, Elite')
print('How many years have you been in the force? ')


age = int(input())

if age <= 5:
    print('Amateur')
elif age > 5 and age <= 10:
    print('Professional')
elif age > 10 and age <= 20:
    print('Veteran')
elif age > 20:
    print('Elite')
else:
    print('wrong input please try again')

number = int(input("Please enter a number:"))

if number > 5:
    print("%s is greater than 5" % number)
elif number < 5:
    print("%s is less than 5" % number)
else:
    print("%s is not greater than, or less than 5. Therefore, %s must be equal to 5." % (number, number))



userAge = int(input("What's your age?"))

if userAge < 0:
    print('“Sorry. I can’t tell what drink because that age is incorrect!”')
elif userAge < 14:
    print('“Drink Toddy”')
elif userAge <18:
    print(' “Drink Coke”')
elif userAge <21:
    print('“Drink Beer”')
elif userAge <130:
    print('“Drink Whisky”')
else:
    print('“Sorry. I can’t tell what drink because that age is incorrect!”')