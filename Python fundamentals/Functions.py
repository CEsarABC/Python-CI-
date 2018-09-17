def greet():
    name1 = input('who do I have the pleasure to talk to? ')
    print('hello to you ' + name1.upper())


greet()

# function definition with parameter
def print_message(name):
    print("Hello %s" % name)

# parameter definition
username = input("What's your name?")

# calling the function
print_message(username)