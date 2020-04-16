'''join string '''

print(','.join(['apple','banana','apple']))

print(':'.join(['apple','banana','apple']))

print(' : '.join(['apple','banana','apple']))

'''replace function'''

print('--------------------------')
print('hello there amandine'.replace('there','world'))

string_1 = 'good morning beautiful world'
string_2 = string_1.replace('morning','afternoon')
print(string_1)
print(string_2)

print('--------------------------')
'''check the string starting point and ending point'''
string_3 = 'checking the new string'
print(string_3.startswith('checking'))
print(string_3.endswith('string'))

print('--------------------------')
'''Upper case and lower case'''
string_4 = string_3.upper()
print(string_4)
string_4 = string_4.lower()
print(string_4)

'''check any content in the string'''
print('--------------------------')
string_5 = "today i'm in bordeaux and is a beautiful day in paradise"
x = 'ay' in string_5
print(x)
y = 'aux'
if y in string_5:
    print(string_5)
else:
    print('{0}, not present in string'.format(y))
print('--------------------------')
p = 'auxi'
if p in string_5:
    print(string_5)
else:
    print('{0}, not present in string'.format(p))
