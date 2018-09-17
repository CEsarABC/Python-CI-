global_variable = 'world'


def print_message():
    print('hello %s' % global_variable)


print_message()


def print_message():
    my_local_variable = "World"
    print("Hello %s" % my_local_variable)

print_message()
print(my_local_variable)