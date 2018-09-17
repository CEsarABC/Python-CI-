def print_message(name):
    print("Hello %s" % name)


username = input("What's your name?")
print_message(username)


def print_message(name="World"):
    print("Hello %s" % name)


username = input("What's your name?")


print_message()
print_message(username)