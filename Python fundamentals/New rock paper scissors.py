from random import randint


options = ['rock', 'paper', 'scissors']


def computer_choice():
    choices = options
    choice_index = randint(0, 2)
    choice = choices[choice_index]
    return choice


compC = computer_choice()

print(compC)

userInput = input('Please chose rock, paper or scissors: ')

print('computer choice is: %s' % compC)


if userInput in options:
    print('your choice is: %s ' % userInput)
else:
    print('wrong choice!')



def compare():

    if compC == userInput:
        print('Draw')

    elif compC == options[0] and userInput == options[1]:
        print('human wins1')

    elif compC == options[0] and userInput == options[2]:
        print('computer wins2')

    elif compC == options[1] and userInput == options[0]:
        print('computer wins3')

    elif compC == options[2] and userInput == options[0]:
        print('human wins4')

    elif compC == options[2] and userInput == options[1]:
        print('computer wins5')

    else:
        print('everything is wrong')


compare()
