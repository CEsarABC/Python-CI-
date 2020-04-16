
def is_even(numbers):
    return numbers % 2 == 0


def number_of_evens(numbers):
    evens = sum([1 for n in numbers if is_even(n)])
    return False if evens == 0 else is_even(evens)

# this is my function to bring the even of evens

"""def number_of_evens(numbers):
    return 0"""

# building tests

# test what we expect to get is equal to actual
def test_are_equal(actual, expected):
    assert expected == actual, "Expected {0}, got {1}".format(expected, actual)
    print('they are equal')

# test what we get is not what we have
def test_not_equal(a, b):
    assert a != b, "Did not expect {0} but got {1}".format(a, b)

# test item is in collection
def test_is_in(collection, item):
    assert item in collection, "{0} does not contain {1}".format(collection, item)

def test_not_in(collection, item):
    assert item not in collection, "{0} is not in {1}".format(item, collection)

def test_is_bigger_than_50(collection, item):
    assert item in collection > 50, "{0} is not bigger than {1}".format(collection, item)

def test_is_less_than_100(collection, item):
    assert item in collection < 100, "{0} is not less than {1}".format(collection, item)

# tests equal number of evens = 0, expected 2
test_are_equal(number_of_evens([1, 2, 3, 4, 5]), 2)

# tests equal number of evens = 2, expected 2
test_are_equal(number_of_evens([1, 2, 3, 11, 5,13, 8]), 2)

#test not equal
test_not_equal(0, 0)

#test not equal
test_not_equal(number_of_evens([1]), 2)
