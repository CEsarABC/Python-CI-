
user = 'cesar'
password = '1234'

if user == 'cesar' and password == '1234':
    print('access granted')
else:
    print('invalid user')

january = ['malena', 'paola', 'roberta', 'chiara']
february = ['rosario', 'zoe', 'renata', 'lorena', 'chiara']

age = list(range(17,60))

name = input('your name please: ')
userAge = input('enter your age: ')

if name in january and userAge in age:
    print('your exam is coming on January')
elif name in february and userAge in age:
    print('your exam is on february')
else:
    print('wrong!!')

circuit1 = True
circuit2 = True
switch1 = True
switch2 = True

if circuit1 and circuit2 and switch1:
    print('everything is in order')

circuit2 = False

if not circuit2 and circuit1 and switch2:
    print('circuit 2 is disconected')

print(age)
print(type(february))
print(january[0][0])

# how to print all names starting with a particular letter ???
#if (january[][0]) == 'm':
#    print(january[][0])