

# We think about and write tests to drive the behaviour
# of an individual function. We can then use extra tests
# to refactor and add extra functionality.

"""now that we see the code is working we can clean the code"""

# (DRY) principle don't repeat yourself


def is_even(number):
    return number % 2 == 0


def even_number_of_evens(numbers):
    if numbers  == []:  # checking is false (no needed anymore)
        return False
    else:
        evens = 0
    for n in numbers:
        if is_even(n):    #(we can substitute this for a function line 12)
            evens += 1
    if evens == 0:
        return False
    else:
        return is_even(evens)


assert even_number_of_evens([]) == False, "No numbers"
assert even_number_of_evens([2]) == False, "One even number"
assert even_number_of_evens([2, 4]) == True, "Two even numbers"
assert even_number_of_evens([2, 3]) == False, "Two numbers, only one even"
assert even_number_of_evens([2, 3, 9, 10, 13, 7, 8]) == False, "Multiple numbers, three even"
assert even_number_of_evens([2, 3, 9, 10, 13, 7, 8, 5, 12]) == True, "Multiple numbers, four even"
assert even_number_of_evens([1, 3, 9]) == False, "No even numbers"

print("All tests passed!")

print(even_number_of_evens([2,3,4,5,6,7,8]))
print(even_number_of_evens([2,6,4]))
print(even_number_of_evens([2,3,4]))