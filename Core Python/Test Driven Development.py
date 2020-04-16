
# we have a function which we will build incrementally
# 1. we build the function
# my function wants to check for the even number of evens in an array


def even_numbers_of_evens(numbers):
    return False

# any function which returns false will pass

# the tests will then print a massage if they pass

print('all tests passed')

# now we star by creating cases which need to be met ny my function


def even_numbers_of_evens1(numbers):
    return False


assert even_numbers_of_evens1([]) == False, 'we expect this to be false in our function'
#assert even_numbers_of_evens1([2,4]) == True, 'we expect this to be true'

# in order for assertion 2 to pass we need to build the function to be able to pass

print('all tests passed')

# this first part is checking if numbers is an empty array or an array with elements

def even_numbers_of_evens1(numbers):
    if numbers  == []:
        return False
    else:
        return True


assert even_numbers_of_evens1([]) == False, 'we expect this to be false in our function'
assert even_numbers_of_evens1([2,4]) == True, 'we expect this to be true'

# check passes. empty array expected to be false and array with elements expected to be true

print('all tests passed')

# now we check other cases

def even_numbers_of_evens1(numbers):
    if numbers  == []:
        return False
    else:
        evens = 0   # starting a variable to count if array is not empty

    for n in numbers:  # we create a loop to count a particular number which will fit ( n % 2 == 0)
        if n % 2 == 0:
            evens += 1  # if a number which fill the description exists (evens) will sum 1 every time it finds a number
    if evens == 0:      # in this case we need to add evens being 0 to return false ( 0 counts as even )
        return False

    return evens % 2 == 0   # the last check will return the evens of evens


# we create our last case but we need to keep building the function

assert even_numbers_of_evens1([]) == False, 'we expect this to be false in our function'
assert even_numbers_of_evens1([2,4]) == True, 'we expect this to be true'   # even number of evens
assert even_numbers_of_evens1([2]) == False, 'we expect this to be false'

assert even_numbers_of_evens1([1,3,9]) == False, 'we expect this to be false'
# this fails because (0 % 2 = 0) so we add to the function the case (line 55)

assert even_numbers_of_evens1([1,3,9,10]) == False, "expect false"

# check passes. empty array expected to be false and array with elements expected to be true

print('all tests passed')