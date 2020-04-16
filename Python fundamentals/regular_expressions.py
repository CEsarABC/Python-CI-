import re

pattern = r"eggs"

if re.match(pattern,"eggseggseggsbacon"):# looks at the start of the string
    print('match found')
else:
    ('no match found')

if re.match(pattern,"baconseggseggsbacon"):# eggs is not at the beggining
    print('match found')
else:
    print('no match found')

if re.search(pattern,"baconseggseggsbacon"):# looks for the letters inside the strng
    print('match found')
else:
    print('no match found')

if re.findall(pattern,"baconseggseggsbacon"):# looks for the letters inside the strng and counts the times is found
    print('match found')
    print(re.findall(pattern,"baconseggseggsbacon"))
    variable = re.findall(pattern,"baconseggseggsbacon")
    print(variable)
    print(type(variable))
else:
    print('no match found')
