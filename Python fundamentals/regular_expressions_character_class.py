import re

# AA1

pattern = r"[A-Z][A-Z][0-9]"
sample = 'AH5'
if re.search(pattern, sample):
    print('Matched')

pattern2 = r"[A-Z][A-Z][0-9][a-z]"
sample2 = 'AH5f'
if re.search(pattern2, sample2):
    print('Matched')

pattern3 = r"[A-Z][A-Z][0-9][A-Z][a-z]"
sample3 = 'AA5Aa'
if re.search(pattern3, sample3):
    print('Matched')
else:
    print('not matched')

def get_password():
    pattern_password = r"[a-z][A-Z][0-9][A-Z]"
    password = input('please enter password: ')
    if re.search(pattern_password, password):
        print('password accepted {}'.format(password))
    else:
        print('password not accepted')

game = True

while game:
    get_password()
    continue_game = input('try another password? y/n ')
    if continue_game.lower() == 'y':
        print('yes continue')
    elif continue_game.lower() == 'n':
        print('closing')
        game = False
    else:
        print('not an option')

print('thanks for coming')
