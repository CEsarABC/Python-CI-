import re

string = 'my name is cesar, hi mr cesar'
pattern = r"cesar"

new_string = re.sub(pattern,'Oscar', string)
print(new_string)

string1 = 'eggSeggeggegg'
pattern1 = r"egg"

new_string1 = re.sub(pattern1,'Oscar', string1)
print(new_string1)
