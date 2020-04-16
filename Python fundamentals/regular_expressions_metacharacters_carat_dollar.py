import re
'''^ is the beggining, $ is the end'''
pattern = r"^gr.y$"

if re.match(pattern,"griy"):
    print('match found')
else:
    print('not found')

if re.match(pattern,"gridsfdfsdfy"):
    print('match found')
else:
    print('not found')

if re.search(pattern,"gridsfsdfy"):
    print('match found')
else:
    print('not found')
print(
'-----------------------------------'
)
pattern2 = r"^grey$"

if re.match(pattern2,"wolfgrey"):
    print('match found')
else:
    print('not found')

if re.match(pattern2,"grey"):
    print('match found')
else:
    print('not found')
