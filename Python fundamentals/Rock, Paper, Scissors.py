from random import randint

print('Rocks, Paper and Scissors game!!!\n'
      'Please choose an option\n'
      '(R), (P), (S)')

optionList = ['rock', 'paper', 'scissors']

my_option = input('give me your option: ')
my_optionLower = my_option.lower()

if my_optionLower == 'r':
    print('your choice: %s' % optionList[0])

elif my_optionLower == 'p':
    print('your choice: %s' % optionList[1])

elif my_optionLower == 's':
    print('your choice: %s' % optionList[2])

else:
    print('just 3 options R, P, S, please try again')

def compOption():
    numbers = []
    for number in range(1, 3):
        numbers.append(randint(1, 1))
        return numbers


# print(compOption())


if compOption() == [1]:
    print('computer choice: rock')
elif compOption() == [2]:
    print('computer choice: paper')
elif compOption() == [3]:
    print('computer choice: scissors')
else:
    print('wrong computer choice')

def game():
    if my_optionLower == 'r' and compOption() == [1]:
        print('DRAW!!')
    elif my_optionLower == 'p' and compOption() == [2]:
        print('DRAW!!')
    elif my_optionLower == 's' and compOption() == [3]:
        print('DRAW!!')
    elif my_optionLower == 'r' and compOption() == [2]:
        print('COMPUTER WINS!!')
    elif my_optionLower == 'r' and compOption() == [3]:
        print('HUMAN WINS!!')
    elif my_optionLower == 'p' and compOption() == [1]:
        print('HUMAN WINS!!')
    elif my_optionLower == 'p' and compOption() == [3]:
        print('COMPUTER WINS!!')
    elif my_optionLower == 's' and compOption() == [1]:
        print('computer wins WINS!!')
    elif my_optionLower == 's' and compOption() == [2]:
        print('HUMAN WINS!!')



game()