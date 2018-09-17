
'''Dictionaries allow us to take things a step further when it comes
 to storing information in a collection. Dictionaries will enable us
  to use what are called key/value pairs. When using a dictionary,
   we define our key/value pairs enclosed in curly braces ({}).
   After that, we use a string as our key. Then we use a colon to
   separate the key from the value, and then we have the value.'''


user = {
    'username': 'zombie',
    'first name': 'Cesar',
    'second name': 'Bernal',
    'age': 35
}

print(user)

# accessing the values similar to indexing
print(user['age'])
print(user['first name'])
print('\n')

# prints the keys
for item in user:
    print(item)

print('\n')

# prints the value of every key
for item in user:
    print(user[item])


#If we needed access to both, keys, and values, we’d have to use a dictionary method called .items().


for key, value in user.items():
    print("Key: %s" % key)
    print("Value: %s" % value)
    print("------------------")