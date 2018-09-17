'''
We can slice up lists to get subsets of a list.
For example, if we wanted to get the first two items in a list,
then we would do the following:
'''

fruits = ["apple", "banana", "peach", "pear", "plum", "orange", "guava", "granadine", "papaya", "mandarin"]

print(fruits[0:2])

print(fruits[:2])

print(fruits[4:])

print(fruits[:])

#In addition to the start: stop values, we also have step. Again, this works in the same way as the range function.

print(fruits[0:9:2])

# reverse list

print(fruits[::-1])

print(fruits[:9])