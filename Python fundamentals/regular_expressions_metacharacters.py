import re
'''have as many dots as characters between the letters'''
pattern = r"gr....y"

if re.match(pattern,'grSSSSy'):
    print('match found')
else:
    print('not found')

pattern2 = r"gr.y"

if re.match(pattern2,'grSy'):
    print('match found')
else:
    print('not found')
