import re

email_pattern = re.compile(r'''(
[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+(\.[a-zA-Z]{2,6})
)''',re.VERBOSE)

text = 'my mail address is giles@whatever.com , but please do not send me spam'

match = email_pattern.search(text)
print(match)
d = match.group()
print(d)

e = match.start()
print(e)

f = match.end()
print(f)

g = match.span()
print(g)
