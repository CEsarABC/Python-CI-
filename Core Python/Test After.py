'''def count_uper_case(message):
    count= 0
    for c in message:
        if c.isupper():
            count += 1
    return count'''

def count_upper_case(message):
    return sum([1 for c in message if c.isupper()])


print(count_upper_case('Hello World of Tanks'))


''' this assertions check for cases and compares what the function returns,
  assert is using the function count with different options,
  the result is what is expected after the counter function is active'''

assert count_upper_case('') == 0, 'empty string'   # count of empty strings  = 0
assert count_upper_case('AA') == 2, 'One upper case' # count of upper case should give two
assert count_upper_case('a') == 0, 'One lower case'
assert count_upper_case('$%&') == 0, 'Special characters'

print('the test passed')


x = 10
y = 20

print(x * y)
print(x-y)
