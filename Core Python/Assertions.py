
"""An assertion is a special type of statement in Python"""

x = 3
y = 2
assert x > y, 'x should be less than y'

print(x + y)

x1 = 1
y1 = 3

assert x1 > y1, '{0} should be less than {1}'.format(x, y)

print(x1 + y1)

