# Using functions to abstract pieces makes it easier to reuse code and concepts.
#  One of the perks of this is that we only need to update our code in one place
# and those changes will be propagated throughout a more extensive system

def get_user_input(prompt):
    return input(prompt)

def print_out_to_console(value_to_be_printed):
    print(value_to_be_printed)

name = get_user_input("Input your name:")
age = get_user_input("Input your age:")

print_out_to_console("Your name is %s" % name)
print_out_to_console("You are %s years old" % age)