import re

game = True

while game:
    pattern_password = r"[a-z][A-Z][0-9][A-Z]"
    password = input('please enter password: ')
    password_b = input('please verify password: ')
    if password != password_b:
        print('verification is different try again')
        continue_game = input('try another password? y/n ')
        if continue_game.lower() == 'y':
            print('yes continue')
        elif continue_game.lower() == 'n':
            print('closing')
            #break
            game = False
        else:
            print('not an option')
    elif re.search(pattern_password, password) and password == password_b:
        print('password accepted!! {}'.format(password))
        print('password saved!!')
        game = False
        #break
    else:
        print('password not accepted check password and verification')
        continue_game = input('try another password? y/n ')
        if continue_game.lower() == 'y':
            print('yes continue')
        elif continue_game.lower() == 'n':
            print('closing')
            #break
            game = False
        else:
            print('not an option')

print('see you soon Amandine!')
